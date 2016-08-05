#!/usr/bin/env python
import sys
from lib import connection

# If you wanted to connect to a broker on a differentmachine,
# you simply specify itsname or IP address here.
channel = connection.connection.channel()

channel.queue_declare(queue=connection.args.queue)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,
                      queue=connection.args.queue ,
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()