# coding=utf-8
"""
记负均正

首先输入要输入的整数个数n，然后输入n个整数。输出为n个整数中负数的个数，和所有正整数的平均值。
"""


class Solution(object):
    def statistic_number(self, data):
        neg_count = len(filter(lambda x: x < 0, data))
        pos_count = len(filter(lambda x: x > 0, data))
        sum_res = sum(filter(lambda x: x > 0, data))
        if sum_res % pos_count == 0:
            return "%d %d" % (neg_count, 0 if pos_count == 0 else sum_res // pos_count)
        else:
            return "%d %.1f" % (neg_count, sum_res / float(pos_count))


def main():
    n = input()
    data = []
    for i in xrange(n):
        data.append(input())
    print Solution().statistic_number(data)


if __name__ == '__main__':
    main()
