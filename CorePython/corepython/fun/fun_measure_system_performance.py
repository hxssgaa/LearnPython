import time
from threading import Lock

lock = Lock()


def statistics(prompt_start=False):
    def statistics_inner(f):
        def wrapper(*arg):
            if prompt_start:
                with lock:
                    print("Function:%s start to run." % f.__name__)
            st = time.time()
            res = f(*arg)
            end = time.time()
            with lock:
                print("Function:%s costs %ss time." % (f.__name__, end - st))
            return res

        return wrapper

    return statistics_inner


@statistics()
def cpu_1():
    return reduce(lambda r, x: r + x, [i for i in xrange(10000000)])


print cpu_1()
