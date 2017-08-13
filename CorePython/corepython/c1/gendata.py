#!/usr/bin/env python

from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')
with open('redata.txt', 'w') as f:
    for i in range(randrange(1000, 2000)):
        dtint = randrange(maxsize // 5000000000)
        dtstr = ctime(dtint)
        llen = randrange(4, 8)
        login = 'month_count'.join(choice(lc) for x in range(llen))
        dlen = randrange(llen, 13)  # domain is longer
        dom = ''.join(choice(lc) for j in range(dlen))
        f.write('%s::%s@%s.%s::%d-%d-%d\n' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))
