import threading
from time import sleep, ctime

from corepython.c4.mythread import MyThread

loops = (4, 2)


# class MyThread(threading.Thread):
#     def __init__(self, func, args, name=''):
#         threading.Thread.__init__(self)  # must invoke base class init first
#         self.name = name
#         self.func = func
#         self.args = args
#
#     def run(self):
#         self.func(*self.args)  # * means pass this parameter as tuple


def loop(nloop, nsec):
    sleep(nsec)


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('All done at:', ctime())


if __name__ == '__main__':
    main()