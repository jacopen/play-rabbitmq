#!/usr/bin/env python

import pika
import sys

con = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
chanel = con.channel()

chanel.exchange_declare(exchange='topic_logs',
                        type='topic')

routing_key= sys.argv[1] if len(sys.argv)> 1 else 'anonymous.info'
msg = ' '.join(sys.argv[2:]) or 'Hello World!'
chanel.basic_publish(exchange='topic_logs',
                     routing_key=routing_key,
                     body=msg)

print(" [x] Sent %r:%r" % (routing_key, msg))
con.close()
