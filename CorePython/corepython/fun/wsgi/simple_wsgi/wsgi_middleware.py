from webob import exc
from webob.dec import wsgify


@wsgify.middleware
def auth_filter(request, app):
    if request.headers.get('X-Auth-Token') != 'open-sesame':
        raise exc.HTTPForbidden
    return app(request)


def filter_factory(global_config, **local_config):
    return auth_filter
