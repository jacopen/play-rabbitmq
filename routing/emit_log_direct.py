#!/usr/bin/env python

import pika
import sys

con = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
chnl = con.channel()

chnl.exchange_declare(exchange='direct_logs', type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'HelloWorld!'
chnl.basic_publish(exchange='direct_logs',
                   routing_key=severity,
                   body=message)

print(" [x] Sent %r:%r" % (severity, message))
con.close()
