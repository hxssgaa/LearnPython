from oj.exception import Error
from oj.common import wsgi
from oj.common.wsgi import render_exception
from provider import Manager

# Header used to transmit the auth token
AUTH_TOKEN_HEADER = 'X-Auth-Token'


class AuthMiddleware(wsgi.Middleware):
    def __init__(self, application):
        self.token_provider_api = Manager()
        super(AuthMiddleware, self).__init__(application)

    def process_request(self, request):
        try:
            self.token_provider_api.get_token_user(request.headers.get(AUTH_TOKEN_HEADER))
        except Error as e:
            return render_exception(e)
