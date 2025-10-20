import os
import boto3
import time

queue_url = "https://sqs.us-east-1.amazonaws.com/440848399208/xxxxx"
sqs = boto3.client('sqs')

# def delete_message(queue_url, receipt_handle):
#     try:
#         response = sqs.delete_message(
#             QueueUrl=queue_url,
#             ReceiptHandle=receipt_handle
#         )
#         print(f"Response: {response}")
#     except Exception as e:
#         print(f"Error deleting message: {e}")
#         raise e

def get_message(queue_url):
    # try to get any messages with message-attributes from SQS queue:
    try:
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MessageSystemAttributeNames=['All'],
            MaxNumberOfMessages=1,
            VisibilityTimeout=60,
            MessageAttributeNames=['All'],
            WaitTimeSeconds=30
        )
#         receipt_handle = response['Messages'][0]['ReceiptHandle']
#         delete_message(queue_url, receipt_handle)

        print(f"{response}")

        # print the MessageAttributes:
#         print(f"MessageAttributes: {response['Messages'][0]['MessageAttributes']}")

        # print the order_no:
#         print(f"Order No: {response['Messages'][0]['MessageAttributes']['order_no']['StringValue']}")
        return response['Messages'][0]

    except Exception as e:
        print(f"Error getting message: {e}")
        raise e

if __name__ == "__main__":
    get_message(queue_url)
