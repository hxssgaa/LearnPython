import simplejson as json

from oj import exception
from oj.common import wsgi
from oj.middleware.auth import AUTH_TOKEN_HEADER
from oj.middleware.provider import Manager as IdentityManager
from provider import Manager as ExamManager


class Auth(wsgi.Application):
    def __init__(self):
        self.identity_api = IdentityManager()
        self.exam_api = ExamManager()

    def commit_exam(self, request):
        user = self.identity_api.get_token_user(request.headers.get(AUTH_TOKEN_HEADER))
        body = json.loads(request.body)
        oj_data = body.get('oj_data', None)
        oj_id = int(body.get('oj_id', None))
        oj = self.exam_api.commit_exam(oj_data, oj_id, user.id)
        return {'result': oj}

    def get_exam(self, request):
        user = self.identity_api.get_token_user(request.headers.get(AUTH_TOKEN_HEADER))
        try:
            oj_id = int(request.params.get('oj_id', -1))
        except ValueError:
            raise exception.ParameterNotValid('parameter oj_id is wrong.')
        oj = self.exam_api.get_exam(oj_id, user.id)
        return {'result': oj}
