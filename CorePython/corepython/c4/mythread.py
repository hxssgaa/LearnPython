import threading


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)  # must invoke base class init first
        self.name = name
        self.func = func
        self.args = args
        self.res = None

    def getResult(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)  # * means pass this parameter as tuple


__name__ = 'mythread'
