import pika
import time

# Establish connection parameters for RabbitMQ
connection_parameters = pika.ConnectionParameters('localhost')

# Create a blocking connection to RabbitMQ
connection = pika.BlockingConnection(connection_parameters)

# Create a communication channel
channel = connection.channel()

# Declare a queue named 'letterbox'
channel.queue_declare(queue='letterbox')

# Send 50 messages to the queue, with a 2-second delay between each
for i in range(1, 51):
    message = f"Hello, this is message number {i}"
    channel.basic_publish(exchange='', routing_key='letterbox', body=message)
    print(f"Sent message: {message}")
    time.sleep(0.5)  # Wait for 2 seconds before sending the next message

# Close the connection
connection.close()

