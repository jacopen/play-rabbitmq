#!/usr/bin/env python

import sys
from lib import connection

# If you wanted to connect to a broker on a differentmachine,
# you simply specify itsname or IP address here.
channel = connection.connection.channel()

channel.queue_declare(queue=connection.args.queue)
channel.basic_publish(exchange='',
                      routing_key=connection.args.routing,
                      body=connection.args.body)

print(" [x] Sent '%s'" % connection.args.body)

connection.connection.close()
