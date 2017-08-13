# coding=utf-8
"""
找出字符串中第一个只出现一次的字符

找出字符串中第一个只出现一次的字符
"""
from collections import defaultdict


class Solution(object):
    def find_first_unique_ch(self, s):
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in s:
            if m[c] == 1:
                return c
        return "."


def main():
    print Solution().find_first_unique_ch(raw_input())


if __name__ == '__main__':
    main()
