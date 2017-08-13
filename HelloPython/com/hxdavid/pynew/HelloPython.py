import json
import random
import sys
from collections import defaultdict
from math import sin, pi
from multiprocessing.pool import Pool
from time import clock

from com.hxdavid.pynew.MyClass import MyClass, MySubClass, Mapping
from com.hxdavid.pynew.MyEntity import MyEntity
from com.hxdavid.pynew.fibo import *

num = 1
text = "123456789"
num2 = 5 ** 2
text2 = "12" * 3 + "24"
print('''
Usage Of this String
is to quote with 3\'
''')

print("#---Strings---")
print(int(text) + num)
print(len(text))
print(num2)
print(text2)
print(text[-1])  # Last character
print(text[-2])  # Second last character
print(text[-2:] == text[len(text) - 2:])
print(text[:2])
print("#---Lists---")

squares = [1, 4, 9, 16, 25]
squares[2] = [1, 2, 3]
print(squares[-1])
print(squares[2:4])
squares.append(64)
squares[2:4] = []
print(squares)
print("#---Arrays---")

a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
print("---Multiple Assignments---")

x = 2
if x < 0:
    x = 0
    print("x < 0")
elif x == 0:
    print("x = 0")
elif x == 1:
    print("Single")
else:
    print("More")

for i in range(3, 9):
    if i % 2 == 0:
        continue
    print(text[i])
print("---For loop and range usage---")


def f(arg=num):
    print(arg)


f(arg=2)  # Keyword Arguments


def concat(*args, sep="/"):
    print("arg len:", len(args))
    return sep.join(args)


print(concat("earth", "mars", "venus"))


def make_increment(n: int):
    """Make increment of function.

    An example of documentation of make_increment.

    :param n: increment start count
    :return: lambda function
    """
    return lambda e: e + n


f = make_increment(42)
print(f(0))
print(f(1))

pairs = [(1, 4), (1, 3), (2, 5), (3, 3)]
pairs.sort(key=lambda e: (e[0], e[1]))  # Sort first by pair[0], then by pair[1], it is key-based and never use cmp.
print(pairs)
print(make_increment.__doc__)

print("---Functions---")

del x
from collections import deque

squares.remove(25)
print(squares)
queue = deque(["a", "b", "c", "d"])
queue.append("e")
queue.append("f")
print(queue.popleft())
print(queue.popleft())
squares = list(map(lambda e: e ** 2, range(10)))  # Crate list by lambda expression
squares2 = [x ** 2 for x in range(10)]
for i in range(0, len(squares)):
    print(squares2[i], end="\t")
    if i % 10 == 9:
        print()
del squares[0]
print(squares)
t = 1, 2, 3, 4, 5  # Tuple
print(t)
basket = {'apple', 'orange', 'basket', 'pear'}  # Set
basket2 = {'apple', 'orange2', 'basket2', 'pear2'}
print('basket' in basket)
print(basket & basket2)
tel = {"a": 4098, "b": 4139, "e": 12, "c": 144, "d": 234}
print(sorted(tel.keys()))
for k, v in sorted(tel.items()):
    print(k, v)

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)
print("---Data Structures---")

print(fib2(1000))
print(str(dir(sys)).format())
json_obj = json.loads('{"a":1,"b":2,"c":3}')
json_str = json.dumps(json_obj)
print(json_str)
print("---Modules---")

try:
    z = 10 * (1 / 0)
except ZeroDivisionError as err:
    print("error detected: ", err)
print("---Exceptions---")


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
x = MySubClass("asd")
print(x.f() == MyClass.f(x))  # Equivalent.
mapping = Mapping(["a", "b", "c"])
print(mapping.items_list)
entity = MyEntity()
entity.name = 'John'
entity.age = 20
entity.salary = 1000
print(entity)
sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print(sine_table)
print("---Classes---")


# def sum_nums(args):
#     return sum(4 * sum({((-1) ** k) / (2 * k + 1) for k in range(0, 1000)}))

def sum_nums(args):
    low = int(args[0])
    high = int(args[1])
    res = sum({((-1) ** k) / (2 * k + 1) for k in range(low, high)})
    return res


jobs = []
n = 10000
procs = 8
sizeSegment = n / procs
for i in range(0, procs):
    jobs.append((i * sizeSegment, (i + 1) * sizeSegment - 1))
pool = Pool(procs).map(sum_nums, jobs)
result = 4 * sum(pool)

print(float(result))
print("---Performance tips---")

somelist = []
for i in range(100000):
    somelist.append((int(random.random() * 10000), int(random.random() * 10000), str(i)))
start = clock()
somelist.sort(key=lambda e: e[1])
end = clock()
print("Sort costs time:" + str(end - start))

somelist.clear()
s = ""
for i in range(1000):
    somelist.append(str(i))  # Avoid this
start = clock()
for substr in somelist:
    s += substr
end = clock()
print("String concatenation 1 costs time:" + str(end - start))
start = clock()
s2 = "".join(somelist)  # Much Much faster
end = clock()
print("String concatenation 2 costs time:" + str(end - start))

head = "a"
prologue = "b"
query = "c"
tail = "d"
out = "<html>" + head + prologue + query + tail + "</html>"  # Avoid this, for performance and readability
out2 = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()  # Use this, much readable and faster
print(out == out2)

oldlist = []
for i in range(1000000):
    oldlist.append("abcdefghijklmn")  # Avoid this
newlist = []
start = clock()
for word in oldlist:
    newlist.append(word.upper())
end = clock()
print("List append 1 costs time:" + str(end - start))

start = clock()
newlist2 = [s.upper() for s in oldlist]
end = clock()
print("List append 2 costs time:" + str(end - start))

start = clock()
iterator2 = (s.upper() for s in oldlist)
end = clock()
print("List append 3(Iterator generator) costs time:" + str(end - start))


def timing(f, n):
    print(f.__name__)
    r = range(n)
    t1 = clock()
    for i in r:
        f()
        f()
        f()
        f()
        f()
        f()
        f()
        f()
        f()
        f()
    t2 = clock()
    print(round(t2 - t1, 3))


"""
Try to use local variables, and avoid dots (use with caution for maintainable).
"""


def func():
    return [s.upper() for s in oldlist]


start = clock()
func()
end = clock()
print("costs time:" + str(end - start))

start = clock()
words = ["%s%s%s" % (random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)) for i in range(100000)]
end = clock()
print("Generate words costs time:" + str(end - start))
wdict = defaultdict(int)
start = clock()
for word in words:
    wdict[word] += 1  # Default dict is fastest way to do this.
end = clock()
print("Word lookup costs time:" + str(end - start))

