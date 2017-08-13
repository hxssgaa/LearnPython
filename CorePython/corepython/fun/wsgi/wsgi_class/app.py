from webob.dec import wsgify
from webob.request import Request
from webob.response import Response


class Hello(object):
    @wsgify(RequestClass=Request)
    def __call__(self, request):
        return Response('Hello, Secret World of WebOb !\n')


def app_factory(global_config, **local_config):
    return Hello()
