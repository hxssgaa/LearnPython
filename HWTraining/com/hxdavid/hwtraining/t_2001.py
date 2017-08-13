# coding=utf-8
"""
将真分数分解为埃及分数

描述
分子为1的分数称为埃及分数。现输入一个真分数(分子比分母小的分数，叫做真分数)，请将该分数分解为埃及分数。
如：8/11 = 1/2+1/5+1/55+1/110。

此题有专门的公式, HW题目可能会出多种结果, 不严谨.

"""


class Solution(object):
    def convert_proper_fraction_to_egypt_fraction(self, a, b):
        res = []
        while b % a != 0:
            c = b // a + 1
            a = a * c - b
            b *= c
            res.append(c)
        res.append(b / a)
        return "+".join(map(lambda x: "1/%d" % x, res))


def main():
    data = raw_input().split('/')
    print Solution().convert_proper_fraction_to_egypt_fraction(int(data[0]), int(data[1]))


if __name__ == '__main__':
    main()
