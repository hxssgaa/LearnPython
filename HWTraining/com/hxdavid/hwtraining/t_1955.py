# coding=utf-8
"""
提取不重复的整数

输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

注意事项:
利用
    OrderedDict.fromkeys(iteratble)
可以得到稳定排序的去重集合
"""
from collections import OrderedDict


class Solution(object):
    def extract_non_repeat_number(self, n):
        return int(''.join(OrderedDict.fromkeys(reversed(str(n)))))


def main():
    print Solution().extract_non_repeat_number(input())


if __name__ == '__main__':
    main()
