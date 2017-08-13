import pika
from pika import PlainCredentials

credential = PlainCredentials('hxssg', '68671388aa')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credential))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print 'Hello World Has been sent!'
connection.close()