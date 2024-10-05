import csv
import random
import csv
import logging
import uuid
import boto3
import polars as pl

from faker import Faker
from datetime import date, datetime, timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.glue import GlueJobOperator
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator

# Configure logging.
logging.basicConfig(
    level=logging.INFO,                    
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

# Get Airflow variables.
S3_BUCKET_NAME = Variable.get('S3_BUCKET_NAME')
S3_FILE_PATH  = Variable.get('S3_FILE_PATH')

local_file_path = "/tmp/raw_data.csv"


def _create_data(locale: str) -> Faker:
    """
    Creates a Faker instance for generating localized fake data.
    Args:
        locale (str): The locale code for the desired fake data language/region.
    Returns:
        Faker: An instance of the Faker class configured with the specified locale.
    """
    # Log the action.
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)


def _generate_record(fake: Faker) -> list:
    """
    Generates a single fake user record.
    Args:
        fake (Faker): A Faker instance for generating random data.
    Returns:
        list: A list containing various fake user details such as name, username, email, etc.
    """
    # Generate random personal data.
    person_name = fake.name()
    user_name = person_name.replace(" ", "").lower()  # Create a lowercase username without spaces.
    email = f"{user_name}@{fake.free_email_domain()}"  # Combine the username with a random email domain.
    personal_number = fake.ssn()  # Generate a random social security number.
    birth_date = fake.date_of_birth()  # Generate a random birth date.
    address = fake.address().replace("\n", ", ")  # Replace newlines in the address with commas.
    phone_number = fake.phone_number()  # Generate a random phone number.
    mac_address = fake.mac_address()  # Generate a random MAC address.
    ip_address = fake.ipv4()  # Generate a random IPv4 address.
    iban = fake.iban()  # Generate a random IBAN.
    accessed_at = fake.date_time_between("-1y")  # Generate a random date within the last year.
    session_duration = random.randint(0, 36_000)  # Random session duration in seconds (up to 10 hours).
    download_speed = random.randint(0, 1_000)  # Random download speed in Mbps.
    upload_speed = random.randint(0, 800)  # Random upload speed in Mbps.
    consumed_traffic = random.randint(0, 2_000_000)  # Random consumed traffic in kB.

    # Return all the generated data as a list.
    return [
        person_name, user_name, email, personal_number, birth_date,
        address, phone_number, mac_address, ip_address, iban, accessed_at,
        session_duration, download_speed, upload_speed, consumed_traffic
    ]


def _write_to_csv() -> None:
    """
    Generates multiple fake user records and writes them to a CSV file.
    """
    # Create a Faker instance with Romanian data.
    fake = _create_data("ro_RO")
    
    # Define the CSV headers.
    headers = [
        "person_name", "user_name", "email", "personal_number", "birth_date", "address",
        "phone", "mac_address", "ip_address", "iban", "accessed_at",
        "session_duration", "download_speed", "upload_speed", "consumed_traffic"
    ]

    # Establish number of rows based date.
    if str(date.today()) == "2024-09-29":
        rows = random.randint(100_372, 100_372)
    else:
        rows = random.randint(0, 1_101)
    
    # Open the CSV file for writing.
    with open(local_file_path, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        # Generate and write each record to the CSV.
        for _ in range(rows):
            writer.writerow(_generate_record(fake))
    # Log the action.
    logging.info(f"Written {rows} records to the CSV file.")


def _add_id() -> None:
    """
    Adds a unique UUID to each row in a CSV file.
    """
    # Load the CSV into a Polars DataFrame.
    df = pl.read_csv(local_file_path)
    # Generate a list of UUIDs (one for each row).
    uuid_list = [str(uuid.uuid4()) for _ in range(df.height)]
    # Add a new column with unique IDs.
    df = df.with_columns(pl.Series("unique_id", uuid_list))
    # Save the updated DataFrame back to a CSV.
    df.write_csv(local_file_path)
    # Log the action.
    logging.info("Added UUID to the dataset.")


def _update_datetime() -> None:
    """
    Update the 'accessed_at' column in a CSV file with the appropriate timestamp.
    """
    # Change date only for next runs.
    if str(date.today()) != "2024-09-29":
        # Get the current time without milliseconds and calculate yesterday's time.
        current_time = datetime.now().replace(microsecond=0)
        yesterday_time = str(current_time - timedelta(days=1))
        # Load the CSV into a Polars DataFrame.
        df = pl.read_csv(local_file_path)
        # Replace all values in the 'accessed_at' column with yesterday's timestamp.
        df = df.with_columns(pl.lit(yesterday_time).alias("accessed_at"))
        # Save the updated DataFrame back to a CSV file.
        df.write_csv(local_file_path)
        # Log the action.
        logging.info("Updated accessed timestamp.")


def _save_to_s3():
    """
    Save CSV file to S3 bucket.
    """
    # Create daily file.
    DAILY_S3_FILE = S3_FILE_PATH + "_" + str(date.today()) + ".csv"
    # Upload CSV file to S3
    s3_client = boto3.client('s3')
    s3_client.upload_file(local_file_path, S3_BUCKET_NAME, DAILY_S3_FILE)
    # Log the action.
    logging.info("Updated data to S3 bucket.")


def save_raw_data():
    '''
    Execute all steps for data generation.
    '''
    # Logging starting of the process.
    logging.info(f"Started batch processing for {date.today()}.")
    # Generate and write records to the CSV.
    _write_to_csv()
    # Add UUID to dataset.
    _add_id()
    # Update the timestamp.
    _update_datetime()
    # Load data to S3 bucket.
    _save_to_s3()
    # Logging ending of the process.
    logging.info(f"Finished batch processing {date.today()}.")


# Define the default arguments for DAG.
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

# Define the DAG.
dag = DAG(
    'driven_data_pipeline',
    default_args=default_args,
    description='DataDriven Main Pipeline.',
    schedule_interval="0 7 * * *",
    start_date=datetime(2024, 9, 28),
    catchup=False,
)

# Define extract raw data task.
extract_raw_data_task = PythonOperator(
    task_id='extract_raw_data',
    python_callable=save_raw_data,
    dag=dag,
)

# Task to trigger the address Glue job.
transform_address_task = GlueJobOperator(
    task_id='transform_address',
    job_name='staging_dim_address',
    dag=dag
)

# Task to trigger the date Glue job.
transform_date_task = GlueJobOperator(
    task_id='transform_date',
    job_name='staging_dim_date',
    dag=dag
)

# Task to trigger the finance Glue job.
transform_finance_task = GlueJobOperator(
    task_id='transform_finance',
    job_name='staging_dim_finance',
    dag=dag
)

# Task to trigger the person Glue job.
transform_person_task = GlueJobOperator(
    task_id='transform_person',
    job_name='staging_dim_person',
    dag=dag
)

# Task to trigger the network usage Glue job.
transform_network_usage_task = GlueJobOperator(
    task_id='transform_network_usage',
    job_name='staging_fact_network_usage',
    dag=dag
)

# Task to trigger the Glue Crawler for raw data.
update_raw_task = GlueCrawlerOperator(
    task_id='update_raw_data',
    config={'Name': 'raw_driven_data'}
)

# Task to trigger the Glue Crawler for address.
update_address_task = GlueCrawlerOperator(
    task_id='update_address',
    config={'Name': 'staging_dim_address'}
)

# Task to trigger the Glue Crawler for date.
update_date_task = GlueCrawlerOperator(
    task_id='update_date',
    config={'Name': 'staging_dim_date'}
)

# Task to trigger the Glue Crawler for finance.
update_finance_task = GlueCrawlerOperator(
    task_id='update_finance',
    config={'Name': 'staging_dim_finance'}
)

# Task to trigger the Glue Crawler for person.
update_person_task = GlueCrawlerOperator(
    task_id='update_person',
    config={'Name': 'staging_dim_person'}
)

# Task to trigger the Glue Crawler for network usage.
update_network_usage_task = GlueCrawlerOperator(
    task_id='update_network_usage',
    config={'Name': 'staging_fact_network_usage'}
)

# Set the task in the DAG.
extract_raw_data_task >> update_raw_task
update_raw_task >> [transform_address_task, transform_date_task, transform_finance_task, transform_person_task, transform_network_usage_task]
transform_address_task >> update_address_task
transform_date_task >> update_date_task
transform_finance_task >> update_finance_task
transform_person_task >> update_person_task
transform_network_usage_task >> update_network_usage_task
