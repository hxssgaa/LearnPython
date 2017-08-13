from oj.common import wsgi
from oj.middleware.provider import Manager


class Auth(wsgi.Application):
    def __init__(self):
        self.token_provider_api = Manager()

    def authenticate_token(self, request):
        username = request.params['username']
        password = request.params['password']
        return {'token': self.token_provider_api.get_user_token(username, password)}
