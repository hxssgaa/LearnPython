from pecan import expose, redirect, route
from webob.exc import status_map


class RootController(object):
    @expose(generic=True, template='index.html')
    def index(self):
        return dict()

    @expose('json', route='hello_asd')
    def hello(self):
        return {'msg': 'Hello!'}

    @index.when(method='POST')
    def index_post(self, q):
        redirect('https://pecan.readthedocs.io/en/latest/search.html?q=%s' % q)

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)


class ChildController(object):
    @expose()
    def child(self):
        return {'msg': 'Child!'}


route(RootController, 'child', ChildController())
