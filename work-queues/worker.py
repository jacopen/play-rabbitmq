import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')


def callback(ch, method, properties, body):
    print(" [x] Recived %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

channel.basic_consume(callback,
                      queue='task_queue',
                      no_ack=True)

print(' [*] Wating for messages. To exit press CTRL+C')
channel.start_consuming()
