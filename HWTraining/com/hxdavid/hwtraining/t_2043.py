# coding=utf-8
"""
查找组成一个偶数最接近的两个素数

任意一个偶数（大于2）都可以由2个素数组成，组成偶数的2个素数有很多种情况，本题目要求输出组成指定偶数的两个素数差值最小的素数对
"""
import math


class Solution(object):
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def closest_prime_numbers(self, n):
        a, b = (n + 1) // 2 - 1, n // 2 + 1
        while a >= 0 and b <= n and (not self.is_prime(a) or not self.is_prime(b)):
            a -= 1
            b += 1
        return a, b


def main():
    print "\n".join(map(str, Solution().closest_prime_numbers(input())))


if __name__ == '__main__':
    main()
