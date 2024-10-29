import boto3
import json
import logging

# Configure logging.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[logging.StreamHandler()]
)

# Initialize resources.
s3 = boto3.client('s3')
sqs = boto3.client('sqs')
bucket_name = "driven-data-bucket"
file_name = 'streaming_data.json'
queue_url = "https://sqs.eu-central-1.amazonaws.com/<your_aws_account_id>/driven_data_queue"


def get_current_data_from_s3() -> list:
    """
    Fetches current contents of the S3 file, or initializes an empty list if not present.\n
    Returns:
        current_data (list): Retrieved data.
    """
    try:
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        current_data = json.loads(response['Body'].read().decode())
    except s3.exceptions.NoSuchKey:
        current_data = []
    return current_data


def save_to_s3(data) -> None:
    """
    Writes data back to S3.
    """
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=json.dumps(data))


def process_messages() -> None:
    """
    Reads messages from SQS, appends them to the S3 file, and deletes the messages.
    """
    # Retrieve messages from SQS.
    response = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    messages_to_process = []
    receipt_handles = []

    # Extract data and receipt handles for each message
    for message in response.get('Messages', []):
        data = json.loads(message['Body'])
        messages_to_process.append(data)
        receipt_handles.append(message['ReceiptHandle'])

    if messages_to_process:
        # Get current data from S3.
        current_data = get_current_data_from_s3()

        # Append new messages.
        current_data.extend(messages_to_process)

        # Save updated data back to S3.
        save_to_s3(current_data)

        # Delete processed messages from SQS.
        for receipt_handle in receipt_handles:
            sqs.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)


def lambda_handler(event, context) -> dict:
    """
    Run Lambda function.\n
    Args:
        event (dict): Event data.
        context (dict): Context data.
    Returns:
        status (dict): Status and body message.
    """
    process_messages()
    return {
        'statusCode': 200,
        'body': json.dumps('Data processed and saved to S3')
    }
