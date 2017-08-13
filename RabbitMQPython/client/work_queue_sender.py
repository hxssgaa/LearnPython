import sys
import pika
from pika import PlainCredentials


credential = PlainCredentials('hxssg', '68671388aa')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credential))
channel = connection.channel()

channel.queue_declare(queue='task_queue')

message = ' '.join(sys.argv[1:]) or "Hello World yyy.........!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode=2,  # make message persistent
                      ))
print(" [x] Sent %r" % message)
