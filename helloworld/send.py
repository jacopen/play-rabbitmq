#!/usr/bin/env python

import pika

# If you wanted to connect to a broker on a differentmachine,
# you simply specify itsname or IP address here.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sendt 'Hello World!'")

connection.close()
