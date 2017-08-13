from webob import Response
from webob.dec import wsgify


@wsgify
def application(request):
    return Response('Hello, World of WebOb !\n')


def app_factory(global_config, **local_config):
    return application
