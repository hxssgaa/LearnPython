# coding=utf-8
"""
质数因子

功能:输入一个正整数，按照从小到大的顺序输出它的所有质数的因子（如180的质数因子为2 2 3 3 5 ）


详细描述：

函数接口说明：
    public String getResult(long ulDataInput)
输入参数：
         long ulDataInput：输入的正整数
返回值：
        String
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

    def get_prime_factor(self, n):
        fac = []
        while n != 1:
            for i in xrange(2, n + 1):
                if n % i == 0:
                    if not self.is_prime(i):
                        continue
                    n /= i
                    fac.append(i)
                    break
        return fac


def main():
    print ' '.join(map(str, Solution().get_prime_factor(input())))


if __name__ == '__main__':
    main()
