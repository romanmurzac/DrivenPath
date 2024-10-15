import json
import time
import random
import logging
import uuid

from datetime import datetime
from faker import Faker
from kafka import KafkaProducer

# Configure logging.
logging.basicConfig(
    level=logging.INFO,                    
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)


def create_data(locale: str) -> Faker:
    """
    Creates a Faker instance for generating localized fake data.
    Args:
        locale (str): The locale code for the desired fake data language/region.
    Returns:
        Faker: An instance of the Faker class configured with the specified locale.
    """
    logging.info(f"Created synthetic data for {locale.split('_')[-1]} country code.")
    return Faker(locale)


def generate_record(fake: Faker) -> list:
    """
    Generates a single fake user record.
    Args:
        fake (Faker): A Faker instance for generating random data.
    Returns:
        list: A list containing various fake user details such as name, username, email, etc.
    """
    streaming_data = {}
    # Generate random personal data.
    streaming_data["person_name"] = fake.name()
    streaming_data["user_name"] = streaming_data["person_name"].replace(" ", "").lower()
    streaming_data["email"] = f'{streaming_data["user_name"]}@{fake.free_email_domain()}'
    streaming_data["personal_number"] = fake.ssn()
    streaming_data["birth_date"] = str(fake.date_of_birth())
    streaming_data["address"] = fake.address().replace("\n", ", ")
    streaming_data["phone_number"] = fake.phone_number()
    streaming_data["mac_address"] = fake.mac_address()
    streaming_data["ip_address"] = fake.ipv4()
    streaming_data["iban"] = fake.iban()
    streaming_data["accessed_at"] = str(datetime.now())
    streaming_data["session_duration"] = random.randint(0, 36_000)
    streaming_data["download_speed"] = random.randint(0, 1_000)
    streaming_data["upload_speed"] = random.randint(0, 800)
    streaming_data["consumed_traffic"] = random.randint(0, 2_000_000)
    streaming_data["unique_id"] = str(uuid.uuid4())
    logging.info(f"Synthetic data produced.")
    return streaming_data


def create_producer() -> KafkaProducer:
    """
    Creates and returns a Kafka producer.\n
    Returns:
        producer: A KafkaProducer object that can send serialized JSON messages to a Kafka broker.
    """
    # Kafka Producer Configuration.
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    logging.info(f"Producer created successfully.")
    return producer


def produce_data(producer: KafkaProducer, topic: str) -> None:
    """
    Continuously generates synthetic data and sends it to a specified Kafka topic.\n
    Args:
        producer (KafkaProducer): The Kafka producer instance used to send messages to the Kafka broker.
        topic (str): The Kafka topic to which the synthetic data will be sent.
    """
    while True:
        # Generate synthetic data.
        synthetic_data = create_data("ro_RO")
        streaming_data = generate_record(synthetic_data)
        # Send data to Kafka topic.
        producer.send(topic, value=streaming_data)
        logging.info(f"Data sent: {streaming_data}")
        # Wait 1-15 seconds before sending the next message.
        time.sleep(random.randint(1, 15))


if __name__ == "__main__":
    # Logging starting of the process.
    logging.info(f"Started streaming producer process.")

    # Define script variables.
    topic = "driven_data_stream"

    # Create data producer.
    producer = create_producer()

    # Produce and send data.
    produce_data(producer, topic)
