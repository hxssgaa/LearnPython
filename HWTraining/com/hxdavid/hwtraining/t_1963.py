# coding=utf-8
"""
求最小公倍数

正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

最大公约数:(gcd)
最小公倍数:(lcm)
算法如下:

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)
"""


class Solution(object):
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def lcm(self, a, b):
        return a * b // self.gcd(a, b)


def main():
    print Solution().lcm(input(), input())


if __name__ == '__main__':
    main()
