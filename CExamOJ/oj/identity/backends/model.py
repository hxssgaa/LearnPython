class User(object):
    __slots__ = ['id', 'username', 'password']

    def __init__(self):
        self.id = None
        self.username = None
        self.password = None
