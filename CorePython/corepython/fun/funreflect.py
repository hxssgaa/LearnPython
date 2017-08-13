def fun1():
    print "Hello, World 1"


def fun2():
    print "Hello, World 2"


def fun3():
    print "Hello, World 3"


def fun55():
    print "Hello, World 55"


for l in list(locals()):
    if "fun" in l:
        locals()[l]()
