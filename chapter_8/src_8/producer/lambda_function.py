import boto3
import json
import time
import random
import logging
from datetime import datetime
from faker import Faker

# Configure logging.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

# Initialize resources.
sqs = boto3.client('sqs')
queue_url = "https://sqs.eu-central-1.amazonaws.com/<your_aws_account_id>/driven_data_queue"
synthetic = Faker()


def create_data(locale: str) -> Faker:
    """
    Creates a Faker instance for generating localized fake data.\n
    Args:
        locale (str): Country code for which to generate data.
    Returns:
        Faker (Faker): Return a instance of Faker library.
    """
    logging.info(f"Creating synthetic data for {locale}.")
    return Faker(locale)


def generate_record(fake: Faker) -> dict:
    """
    Generates a single fake user record.\n
    Args:
        fake (Faker): Instance of Faker library.
    Returns:
        streaming_data (dict): Generated data.
    """
    streaming_data = {
        "person_name": fake.name(),
        "user_name": fake.name().replace(" ", "").lower(),
        "email": f'{fake.name().replace(" ", "").lower()}@{fake.free_email_domain()}',
        "personal_number": fake.ssn(),
        "birth_date": str(fake.date_of_birth()),
        "address": fake.address().replace("\n", ", "),
        "phone_number": fake.phone_number(),
        "mac_address": fake.mac_address(),
        "ip_address": fake.ipv4(),
        "iban": fake.iban(),
        "accessed_at": str(datetime.now()),
        "session_duration": random.randint(0, 36000),
        "download_speed": random.randint(0, 1000),
        "upload_speed": random.randint(0, 800),
        "consumed_traffic": random.randint(0, 2000000),
        "unique_id": fake.uuid4()
    }
    logging.info("Generated synthetic data record.")
    return streaming_data


def produce_data(time_limit=15) -> None:
    """
    Generates and sends synthetic data to SQS within a set time limit.\n
    Args:
        time_limit (int): Time limit to run Lambda function.
    """
    start_time = datetime.now()
    fake_data_generator = create_data("ro_RO")
    
    while (datetime.now() - start_time).seconds < time_limit * 60:
        streaming_data = generate_record(fake_data_generator)
        logging.info(f"Generated data: {streaming_data}")
        
        # Send generated data to SQS.
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(streaming_data)
        )
        logging.info(f"Sent message ID: {response['MessageId']} to SQS.")

        # Wait 1-15 seconds before sending the next message.
        time.sleep(random.randint(1, 15))


def lambda_handler(event, context) -> dict:
    """
    Run Lambda function.\n
    Args:
        event (dict): Event data.
        context (dict): Context data.
    Returns:
        status (dict): Status and body message.
    """
    # Run data generation process for up to 15 minutes.
    result = produce_data()
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
