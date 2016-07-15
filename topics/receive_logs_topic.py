#!/usr/bin/env python

import pika
import sys

con = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
chanel = con.channel()

chanel.exchange_declare(exchange='topic_logs',
                        type='topic')

result = chanel.queue_declare(exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    chanel.queue_bind(exchange='topic_logs',
                      queue=queue_name,
                      routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

chanel.basic_consume(callback,
                     queue=queue_name,
                     no_ack=True)

chanel.start_consuming()
