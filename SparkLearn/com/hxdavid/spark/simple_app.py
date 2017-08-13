from random import random

from pyspark import SparkContext
from operator import add

if __name__ == '__main__':
    sc = SparkContext("local[8]", "Simple App")
    partitions = 128
    n = 1000000 * partitions


    def f(_):
        x = random() * 2 - 1
        y = random() * 2 - 1
        return 1 if x ** 2 + y ** 2 < 1 else 0


    count = sc.parallelize(range(1, n + 1), partitions).map(f).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))
