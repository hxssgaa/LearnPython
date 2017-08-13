import controllers

from oj.common import wsgi


class Routers(wsgi.ComposableRouter):
    def add_routes(self, mapper):
        controller = controllers.Auth()
        self._add_resource(
            mapper, controller,
            path='/exams',
            post_action='commit_exam',
            get_action='get_exam',
        )
