# coding=utf-8
"""
字符个数统计

编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。
"""


class Solution(object):
    def char_stat(self, s):
        return len(set(filter(lambda x: 0 <= ord(x) <= 127, s)))


def main():
    print Solution().char_stat(raw_input())


if __name__ == '__main__':
    main()
