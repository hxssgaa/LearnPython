# coding=utf-8
"""
名字的漂亮度

给出一个名字，该名字有26个字符串组成，定义这个字符串的“漂亮度”是其所有字母“漂亮度”的总和。
每个字母都有一个“漂亮度”，范围在1到26之间。没有任何两个字母拥有相同的“漂亮度”。字母忽略大小写。
给出多个名字，计算每个名字最大可能的“漂亮度”。

a b c d e f g h i j k l m n o p q r s t u v w x y z
zhangsan
aanngszh  26*2+25*2+24+23+22+21 52+50+24+23+22+21=126+23+22+21

此题的格式非常坑,竟然是输出需要换行,但是题目并没有说明,也就是说格式是每个字符串对应输入一行就输出一行.
"""
from collections import defaultdict


class Solution(object):
    @staticmethod
    def calculate_beauty(name):
        m = defaultdict(int)
        for e in name:
            m[e] += 1
        v = sorted(m.values(), reverse=True)
        return sum((26 - i) * e for i, e in enumerate(v))


def main():
    n = input()
    for _ in range(n):
        print Solution.calculate_beauty(raw_input())


if __name__ == '__main__':
    main()
