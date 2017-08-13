import sys

import pika
from pika import PlainCredentials

credential = PlainCredentials('hxssg', '68671388aa')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credential))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
