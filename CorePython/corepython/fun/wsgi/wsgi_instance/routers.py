# coding=utf-8
import routes
import routes.middleware
import webob
import webob.dec
from webob.dec import wsgify

import controllers


class Router(object):
    def __init__(self):
        # 创建Mapper对象，用于URL解析
        self.mapper = routes.Mapper()
        # 在Mapper中添加URL映射
        self.add_routes()
        # 创建RoutesMiddleware对象，用于URL分发
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)

    def add_routes(self):
        controller = controllers.Controller()
        self.mapper.connect("/instances",
                            controller=controller, action="create",
                            conditions=dict(method=["POST"]))

        self.mapper.connect("/instances",
                            controller=controller, action="index",
                            conditions=dict(method=["GET"]))

        self.mapper.connect("/instances/{instance_id}",
                            controller=controller, action="show",
                            conditions=dict(method=["GET"]))

        self.mapper.connect("/instances/{instance_id}",
                            controller=controller, action="update",
                            conditions=dict(method=["PUT"]))

        self.mapper.connect("/instances/{instance_id}",
                            controller=controller, action="delete",
                            conditions=dict(method=["DELETE"]))

    @wsgify(RequestClass=webob.Request)
    def __call__(self, request):
        return self._router

    # 实现HTTP请求的分发
    @staticmethod
    @wsgify(RequestClass=webob.Request)
    def _dispatch(request):
        # 获取URL的解析结果
        match = request.environ['wsgiorg.routing_args'][1]
        if not match:
            return _err()
        app = match['controller']
        return app


def _err():
    return 'The Resource is Not Found.'


def app_factory(global_config, **local_config):
    return Router()
