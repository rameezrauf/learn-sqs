import os
import boto3
import time

queue_url = "https://sqs.us-east-1.amazonaws.com/440848399208/xxxxx"
sqs = boto3.client('sqs')

def send_message(queue_url, message):
# def send_message(queue_url, message, order_no, content):
    try:
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message,
#            MessageAttributes={
#                'order_no': {
#                    'DataType': 'String',
#                    'StringValue': order_no
#                },
#                'word': {
#                    'DataType': 'String',
#                    'StringValue': content
#                }
#            }
        )
        print(f"Response: {response}")

    except Exception as e:
        print(f"Error sending message: {e}")
        raise e

if __name__ == "__main__":
    send_message(queue_url, "Hello, World!")
#    send_message(queue_url, "Hello, World!", "11", "Grapefruit")

