class Entity(object):
    def _get_age(self):
        return self._age

    def _set_age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be set to an integer")
        self._age = value

    age = property(_get_age, _set_age)

    def __init__(self):
        pass
