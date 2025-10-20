# learn-sqs

Learn the AWS SQS, the Simple Queuing Service.

## About SQS

- SQS is an asynchronous messaging service.
- Messages are organized by queue, i.e. "topic".
- Messages are held up to 4 days by default (max 14 days).
- Messages have a "body" (like an email) but can also have additional `MessageAttributes` the sender adds.
- Messages can be received 1 at a time (default) or in groups of up to 10.
- Messages are picked up in random order, unless the queue is created as FIFO.
- Messages that are read are not deleted by default. Deletion must be explicitly performed for each message.
- SQS allows for long polling.
- SQS allows for Dead Letter queues.

## Exercises in this repository:

- [Get queue attributes](get-queue-attributes.py)
- [Send Messages](send-message.py)
- [Receive Messages](receive-message.py)

## Reference

[**boto3 Reference** for SQS](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html)
