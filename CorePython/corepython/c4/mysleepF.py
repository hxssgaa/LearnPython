from atexit import register
from random import randrange
from threading import Thread, currentThread, Lock
from time import sleep, ctime

lock = Lock()


class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)


loops = (randrange(2, 5) for x in range(randrange(3, 7)))
remaining = CleanOutputSet()  # thread.active_count() can just do the same thing


def loop(nsec):
    myname = currentThread().name
    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)
    with lock:
        remaining.remove(myname)
        print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
        print(' (remaining: %s)' % (remaining or 'NONE'))


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause,)).start()


@register
def _atexit():
    print('all DONE at:', ctime())


_main()
