#!/usr/bin/env python

import pika
import sys

con = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
chnl = con.channel()

chnl.exchange_declare(exchange='direct_logs',
                      type='direct')

result = chnl.queue_declare(exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    chnl.queue_bind(exchange='direct_logs',
                    queue=queue_name,
                    routing_key=severity)

print(' [*] Witing for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

chnl.basic_consume(callback,
                   queue=queue_name,
                   no_ack=True)

chnl.start_consuming()
