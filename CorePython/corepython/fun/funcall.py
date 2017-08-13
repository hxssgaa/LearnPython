# coding=utf-8


class Factorial:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):  # 这个类可以当成一个函数使用
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n - 1)
        return self.cache[n]


fact = Factorial()
for i in xrange(1, 40):
    print "%d! = %d" % (i, fact(i))
