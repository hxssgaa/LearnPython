class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self, name):
        self.__name = name  # Private variable
        print("object init")

    def f(self):
        return 'hello, world'

    def _f2(self):
        return 'hello, world 2'

    def __f3(self):
        return 'hello, world 3'


class MySubClass(MyClass):
    def f(self):
        return "hello, world 2"

    def _f2(self):
        return super()._f2()


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def __update(self, iterable):  # Private method
        for item in iterable:
            self.items_list.append(item)
