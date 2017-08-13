import os
import re

from corepython.c4.mythread import MyThread
from corepython.utils.utils import statistics


# Compare the speed of counting lines of files between multiple threads and single thread.

@statistics()
def count_file(d):
    return sum(1 for _ in open(d))


@statistics()
def _main_multiple_thread():
    patt = re.compile("[\w\s]+.txt")
    dirs = [d for d in os.listdir(".") if patt.match(d)]
    threads = [MyThread(count_file, (d,), count_file.__name__) for d in dirs]
    m = {}
    for t in threads:
        t.start()
    for i, t in enumerate(threads):
        t.join()
        m[dirs[i]] = t.getResult()
    print(m)


@statistics()
def _main_single_thread():
    patt = re.compile("[\w\s]+.txt")
    dirs = [d for d in os.listdir(".") if patt.match(d)]
    m = {d: sum(1 for _ in open(d)) for d in dirs}
    print(m)


if __name__ == '__main__':
    _main_single_thread()
