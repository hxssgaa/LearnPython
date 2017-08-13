from threading import Lock
from time import time

lock = Lock()


def statistics(run_count=1, prompt_start=False):
    def statistics_inner(f):
        def wrapper(*arg):
            if prompt_start:
                with lock:
                    print("Function:%s start to run." % f.__name__)
            st = time()
            res = None
            for _ in range(run_count):
                res = f(*arg)
            end = time()
            with lock:
                print("Function:%s costs %ss time." % (f.__name__, (end - st)))
            return res

        return wrapper

    return statistics_inner
