from timeit import timeit

import Extest
import math

math.factorial(12)

print timeit("Extest.fac(10)", setup="import Extest")
print timeit("math.factorial(10)", setup="import math")
print Extest.fac(10)
print math.factorial(10)
print timeit("Extest.doppel(\"asdkasjkdjaskdjaksjdkasjdkajskdjaksdjkasjdkasjdkjk123123123123123adasdasdasdasasda\")", setup="import Extest")
print timeit("\"asdkasjkdjaskdjaksjdkasjdkajskdjaksdjkasjdkasjdkjk123123123123123adasdasdasdasasda\"[::-1]")
print Extest.doppel("asdkasjkdjaskdjaksjdkasjdkajskdjaksdjkasjdkasjdkjk123123123123123adasdasdasdasasda")
print "asdkasjkdjaskdjaksjdkasjdkajskdjaksdjkasjdkasjdkjk123123123123123adasdasdasdasasda"[::-1]