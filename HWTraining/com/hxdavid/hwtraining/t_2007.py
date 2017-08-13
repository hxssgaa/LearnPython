# coding=utf-8
"""
超长正整数相加

请设计一个算法完成两个超长正整数的加法。
"""


class Solution(object):
    def num_str_add(self, s1, s2):
        return str(long(s1) + long(s2))


def main():
    print Solution().num_str_add(raw_input(), raw_input())


if __name__ == '__main__':
    main()
