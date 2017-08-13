from time import time


def main():
    c = time()
    print sum(range(1, 20000000))
    e = time()
    print e - c

if __name__ == '__main__':
    main()
