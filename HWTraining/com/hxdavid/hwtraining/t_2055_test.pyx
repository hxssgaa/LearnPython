# coding=utf-8
"""
iNOC产品部--完全数计算

完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
例如：28，它有约数1、2、4、7、14、28，除去它本身28外，其余5个数相加，1+2+4+7+14=28。
给定函数count(int n),用于计算n以内(含n)完全数的个数。计算范围, 0 < n <= 500000
返回n以内完全数的个数。异常情况返回-1
"""

class Solution(object):
    def count_perfect_number(self, int n):
        cdef int cnt = 0
        cdef int temp_sum = 0
        for i in xrange(1, n + 1):
            temp_sum = 0
            for z in xrange(1, i):
                if i % z == 0:
                    temp_sum += z
            if temp_sum == i:
                cnt += 1
        return cnt
