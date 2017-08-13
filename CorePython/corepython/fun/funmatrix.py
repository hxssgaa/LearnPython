import numpy as np
import random

m1 = [[random.random()] for _ in xrange(10000)]
m2 = [[random.random() for _ in xrange(10000)]]
a = np.matrix(m1)
b = np.matrix(m2)
print "start"
c = a * b
print c
print "(%dX%d)" % (c.shape[0], c.shape[1])
