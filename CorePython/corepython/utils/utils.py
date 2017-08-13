from threading import Lock
from time import time

lock = Lock()


def statistics(prompt_start=False):
    def statistics_inner(f):
        def wrapper(*arg):
            if prompt_start:
                with lock:
                    print("Function:%s start to run." % f.__name__)
            st = time()
            res = f(*arg)
            end = time()
            with lock:
                print("Function:%s costs %ss time." % (f.__name__, end - st))
            return res

        return wrapper

    return statistics_inner
