import pika
from pika import PlainCredentials


credential = PlainCredentials('hxssg', '68671388aa')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/', credential))
channel = connection.channel()


def callback(ch, method, properties, body):
    print 'Received %r' % body


channel.queue_declare(queue='hello')
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
