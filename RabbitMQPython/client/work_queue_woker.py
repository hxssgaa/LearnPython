import time

import pika
from pika import PlainCredentials

credential = PlainCredentials('hxssg', '68671388aa')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credential))
channel = connection.channel()
channel.queue_declare(queue='task_queue')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue',)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
