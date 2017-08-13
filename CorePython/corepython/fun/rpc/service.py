# coding=utf-8
import dispatcher
import manager
import rpc

TOPIC = 'sendout_request'


class Service(object):
    def __init__(self):
        self.topic = TOPIC
        self.manager = manager.Manager()

    def start(self):
        self.conn = rpc.create_connection()                      # 创建RabbitMQ连接
        rpc_dispatcher = dispatcher.RpcDispatcher(self.manager)  # 创建分发器
        self.conn.create_consumer(self.topic, rpc_dispatcher)    # 创建主题消费者
        self.conn.consume()                                      # 主题消费者开始消费

    def drain_events(self):
        self.conn.drain_events()  # 用来处理RPC请求
