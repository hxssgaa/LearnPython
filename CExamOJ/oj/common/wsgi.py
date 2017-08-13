# coding=utf-8
import routes
import routes.middleware
import simplejson
from webob.dec import wsgify
import webob

from oj import exception
from oj.exception import Error


class Application(object):
    @wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        # 获取url解析结果
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        # 获取处理的方法
        action = arg_dict.pop('action')
        # 删除controller项，剩下参数列表
        del arg_dict['controller']
        # 找到方法函数
        method = getattr(self, action)
        # 通过参数列表，和方法函数，执行该方法
        try:
            result = method(req, **arg_dict)
            # 无返回值
            if result is None:
                return webob.Response(body='',
                                      status='204 Not Found',
                                      headerlist=[('Content-Type',
                                                   'application/json')])
            if not isinstance(result, basestring):
                result = simplejson.dumps(result, default=lambda o: o.__dict__, ensure_ascii=False)
            return result
        except Error as e:
            return render_exception(e)


class Middleware(Application):
    """Base WSGI middleware.

    These classes require an application to be
    initialized that will be called next.  By default the middleware will
    simply call its wrapped app, or you can override __call__ to customize its
    behavior.
    """

    @classmethod
    def factory(cls, global_config):
        """Used for paste app factories in paste.deploy config files."""

        def _factory(app):
            return cls(app)

        return _factory

    def __init__(self, application):
        super(Middleware, self).__init__()
        self.application = application

    def process_request(self, request):
        """Called on each request.

        If this returns None, the next application down the stack will be
        executed. If it returns a response then that response will be returned
        and execution will stop here.

        """
        return None

    def process_response(self, request, response):
        """Do whatever you'd like to the response, based on the request."""
        return response

    @wsgify(RequestClass=webob.Request)
    def __call__(self, request):
        response = self.process_request(request)
        if response:
            return response
        response = request.get_response(self.application)
        return self.process_response(request, response)


class RoutersBase(object):
    def __init__(self, mapper):
        self.map = mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.map)

    @wsgify(RequestClass=webob.Request)
    def __call__(self, request):
        return self._router

    @staticmethod
    @wsgify(RequestClass=webob.Request)
    def _dispatch(req):
        """Dispatch the request to the appropriate controller.

        Called by self._router after matching the incoming request to a route
        and putting the information into req.environ.  Either returns 404
        or the routed WSGI app's response.

        """
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            msg = ('(%(url)s): The resource could not be found.' %
                   {'url': req.url})
            return render_exception(exception.NotFound(msg))
        app = match['controller']
        return app

    def _add_resource(self, mapper, controller, path,
                      get_action=None, head_action=None, get_head_action=None,
                      put_action=None, post_action=None, patch_action=None,
                      delete_action=None, get_post_action=None):
        if get_head_action:
            getattr(controller, get_head_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=get_head_action,
                           conditions=dict(method=['GET', 'HEAD']))
        if get_action:
            getattr(controller, get_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=get_action,
                           conditions=dict(method=['GET']))
        if head_action:
            getattr(controller, head_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=head_action,
                           conditions=dict(method=['HEAD']))
        if put_action:
            getattr(controller, put_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=put_action,
                           conditions=dict(method=['PUT']))
        if post_action:
            getattr(controller, post_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=post_action,
                           conditions=dict(method=['POST']))
        if patch_action:
            getattr(controller, patch_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=patch_action,
                           conditions=dict(method=['PATCH']))
        if delete_action:
            getattr(controller, delete_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=delete_action,
                           conditions=dict(method=['DELETE']))
        if get_post_action:
            getattr(controller, get_post_action)  # ensure the attribute exists
            mapper.connect(path, controller=controller, action=get_post_action,
                           conditions=dict(method=['GET', 'POST']))

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls(None)


class ComposableRouter(RoutersBase):
    """Router that supports use by ComposingRouter."""

    def __init__(self, dict):
        mapper = routes.Mapper()
        self.add_routes(mapper)
        super(ComposableRouter, self).__init__(mapper)

    def add_routes(self, mapper):
        """Add routes to given mapper."""
        pass


def get_exception_body(exc):
    return {
        'title': exc.title,
        'message': exc.message,
    }


def render_response(body, status, headers):
    return webob.Response(body=simplejson.dumps(body),
                          status='%d %s' % status,
                          headerlist=headers)


def render_exception(error):
    message = error.args[0]
    body = {'error': {
        'code': error.code,
        'title': error.title,
        'message': message,
    }}
    headers = []
    return render_response(body, (error.code, error.title), headers)
