import controllers

from oj.common import wsgi


class Routers(wsgi.ComposableRouter):
    def add_routes(self, mapper):
        controller = controllers.Auth()
        self._add_resource(
            mapper, controller,
            path='/tokens',
            post_action='authenticate_token'
        )
