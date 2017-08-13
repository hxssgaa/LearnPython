import simplejson
from simplejson.scanner import JSONDecodeError

from oj import exception
from oj.common.utils import AESCipher
import simplejson as json

from oj.identity.backends.model import User

TOKEN_CIPHER_KEY = "hxdavid_c_exam_oj"


class Manager(object):
    def __init__(self):
        self.cipher = AESCipher(TOKEN_CIPHER_KEY)
        self.user_map = self._map_users()

    def _map_users(self):
        users = {}
        with open('data/users.data') as f:
            cnt = int(f.readline())
            for _ in xrange(cnt):
                user = User()
                user.id = int(f.readline().strip('\n'))
                user.username = f.readline().strip('\n')
                user.password = f.readline().strip('\n')
                users[user.id] = user
        return users

    def get_token_user(self, token):
        if not token:
            raise exception.TokenNotFound('No token in the request')
        try:
            token_json = self.cipher.decrypt(token).encode('utf-8')
            user_token = json.loads(token_json)
            return self.get_user(user_id=user_token['user_id'])
        except (JSONDecodeError, ValueError, TypeError, KeyError):
            raise exception.TokenNotValid('No valid token in the request')

    def get_user(self, user_id=None, username=None, password=None):
        if not user_id and not username and not password:
            raise exception.UserNotFound('No user found')
        if user_id and user_id in self.user_map:
            return self.user_map[user_id]
        for v in self.user_map.values():
            if v.username == username and v.password == password:
                return v
        raise exception.UserNotFound('No user found')

    def get_user_token(self, username, password):
        user = self.get_user(username=username, password=password)
        try:
            token_json = simplejson.dumps({
                'user_id': user.id,
            })
            return self.cipher.encrypt(token_json)
        except (JSONDecodeError, ValueError, TypeError):
            raise exception.TokenNotValid('No valid token in the request')


cipher = AESCipher("hxdavid_c_exam_oj")
enc = cipher.encrypt(b"{\"username\":\"admin\", \"password\":\"686713aa\"}")
print enc
dec = cipher.decrypt(enc).encode('utf-8')
print dec
x = json.loads(dec)
print x['username']
print x['password']

#
# def check_user_exists(username, password):
#     with open('./oj/data/users.data') as f:
#         cnt = int(f.readline())
#         for _ in xrange(cnt):
#             data_username, data_password = f.readline(), f.readline()
#             if username == data_password and password == data_password:
#                 return
#     raise exception.TokenNotValid('Username or password is wrong')
