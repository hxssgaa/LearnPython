# coding=utf-8
"""
统计每个月兔子的总数

有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？

此题就是考察fibonacci算法, 利用最高效的迭代法就可以解决:
    def fib(n):
        if n <= 2:
            return 1
        res = a = b = 1
        for i in range(2, n):
            res = a + b
            b = a
            a = res
        return res
"""


class Solution(object):
    def fib(self, n):
        if n <= 2:
            return 1
        res = a = b = 1
        for i in range(2, n):
            res = a + b
            b = a
            a = res
        return res


def main():
    print Solution().fib(input())


if __name__ == '__main__':
    main()
