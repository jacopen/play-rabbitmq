#!/usr/bin/env python
import sys
from lib import connection

# If you wanted to connect to a broker on a differentmachine,
# you simply specify itsname or IP address here.
channel = connection.connection.channel()

channel.exchange_declare(exchange=connection.args.exchange, type='fanout')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange=connection.args.exchange,
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)
channel.start_consuming()
