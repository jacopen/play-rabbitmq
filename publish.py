#!/usr/bin/env python

import sys
from lib import connection

# If you wanted to connect to a broker on a differentmachine,
# you simply specify itsname or IP address here.
channel = connection.connection.channel()

channel.exchange_declare(exchange=connection.args.exchange, type='fanout')
channel.basic_publish(exchange=connection.args.exchange,
                      routing_key=connection.args.routing,
                      body=connection.args.body)

print(" [x] Sent '%s'" % connection.args.body)

connection.connection.close()
