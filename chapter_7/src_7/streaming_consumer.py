import json
import psycopg2
import logging

from kafka import KafkaConsumer

# Configure logging.
logging.basicConfig(
    level=logging.INFO,                    
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)


def read_credentials(file_path: str) -> dict:
    """
    Read database credentials from JSON file.\n
    Args:
        file_path (str): Path to the JSON file containing the database credentials.
    Returns:
        credentials (dict): A dictionary containing database connection credentials.
    """
    # Read the database credentials from a JSON file.
    with open(file_path, 'r') as file:
        credentials = json.load(file)
    logging.info("Read credentials from JSON file.")
    return credentials


def read_sql(file_path: str) -> str:
    """
    Read SQL queries from a file.\n
    Args:
        file_path (str): Path to the SQL file containing the queries.
    Returns:
        sql_query (str): The SQL query as a string.
    """
    # Read the SQL file to retrieve the query.
    with open(file_path, 'r') as sql_file:
        sql_query = sql_file.read()
    logging.info("Read SQL query from sql file.")
    return sql_query


def create_consumer(topic: str) -> KafkaConsumer:
    """
    Creates and returns a Kafka consumer for the given topic.\n
    Args:
        topic (str): The Kafka topic to subscribe to.
    Returns:
        consumer: A KafkaConsumer object that subscribes to the specified topic and consumes messages.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )
    logging.info("Consumer created successfully.")
    return consumer


def connect_db(credentials: dict) -> psycopg2.connect:
    """
    Establish a connection to the PostgreSQL database.\n
    Args:
        credentials (dict): A dictionary containing database connection credentials.
    Returns:
        conn (psycopg2.connect): A connection object to the PostgreSQL database.
    """
    # Connect to the PostgreSQL server using the provided credentials.
    conn = psycopg2.connect(
        dbname=credentials['dbname'],
        user=credentials['user'],
        password=credentials['password'],
        host=credentials['host'],
        port=credentials['port']
    )
    logging.info("Create database connection.")
    return conn


def create_object(conn: psycopg2.connect, creation_query: str) -> None:
    """
    Execute a SQL command to create a database object, a table or schema.\n
    Args:
        conn (psycopg2.connect): A connection object to the PostgreSQL database.
        creation_query (str): The SQL query to create the database object.
    """
    # Open a cursor to perform database operations.
    cursor = conn.cursor()
    # Execute the provided SQL command for creation.
    cursor.execute(creation_query)
    # Commit the changes to the database.
    conn.commit()
    logging.info("Create table / schema.")


def consume_data(conn: psycopg2.connect, consumer: KafkaConsumer, table_name: str) -> None:
    """
    Consumes messages from a Kafka topic and inserts the consumed data into a PostgreSQL database.\n
    Args:
        conn (psycopg2.connect): A connection object for the PostgreSQL database.
        consumer (KafkaConsumer): A Kafka consumer that ingest streaming data.
        table_name (str): The Postgres table name where to ingest data.
    """
    cursor = conn.cursor()
    # Loop through each message from the Kafka consumer.
    for message in consumer:
        # Extract the value from the message.
        data = message.value
        # Get all column names from the message data.
        columns = data.keys()  
        # Get corresponding values for the columns.
        values = [data.get(col) for col in columns]
        # Construct the SQL query with placeholders for the column names and values.
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        # Execute the SQL query with the extracted values.
        cursor.execute(query, values)
        # Commit the transaction to the database.
        conn.commit()
        logging.info(f"Data were consumed: {values}")

    # Close the cursor and the database connection after processing all messages.
    cursor.close()
    conn.close()


if __name__ == "__main__":
    # Logging starting of the process.
    logging.info(f"Started streaming consumer process.")

    # Define script variables.
    credentials_path = "credentials.json"
    schema_path = "create_schema.sql"
    table_path= "create_table.sql"
    topic = "driven_data_stream"
    table_name = "streaming_layer.streaming_data"

    # Get credentials for database connection.
    credentials = read_credentials(credentials_path)

    # Create database connection.
    connection = connect_db(credentials)

    # Create Kafka consumer.
    consumer = create_consumer(topic)

    # Create schema.
    schema_query = read_sql(schema_path)
    schema = create_object(connection, schema_query)

    # Create table.
    table_query = read_sql(table_path)
    table = create_object(connection, table_query)

    # Consume data.
    consume_data(connection, consumer, table_name)
