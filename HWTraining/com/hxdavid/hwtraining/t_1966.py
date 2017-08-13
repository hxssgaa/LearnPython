# coding=utf-8
"""
记负均正

从输入任意个整型数，统计其中的负数个数并求所有非负数的平均值
"""


class Solution(object):
    def negative_statistics(self, data):
        num_neg = len(filter(lambda x: x < 0, data))
        sum_other = sum(filter(lambda x: x >= 0, data))
        num_other = len(data) - num_neg
        if num_other == 0:
            return '%d\n0.0' % num_neg
        else:
            return '%d\n%.1f' % (num_neg, float(sum_other) / num_other)


def main():
    data = []
    while True:
        try:
            data.append(input())
        except EOFError:
            break
    print Solution().negative_statistics(data)


if __name__ == '__main__':
    main()
