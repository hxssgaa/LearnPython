# coding=utf-8
"""
iNOC产品部--完全数计算

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
给定函数count(int n),用于计算n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
返回n以内完全数的个数。异常情况返回-1
"""
from com.hxdavid.utils.utils import statistics
import pyximport; pyximport.install()
from com.hxdavid.hwtraining.t_2055_test import Solution


class Solution2(object):
    @statistics()
    def count_perfect_number(self, n):
        return Solution().count_perfect_number(n)
        # cnt = 0
        # for i in xrange(1, n + 1):
        #     factor = filter(lambda x: i % x == 0, range(1, i))
        #     if sum(factor) == i:
        #         cnt += 1
        # return cnt


def main():
    print Solution2().count_perfect_number(input())


if __name__ == '__main__':
    main()
