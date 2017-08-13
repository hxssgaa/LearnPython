# coding=utf-8
"""
计算字符个数

写出一个程序，接受一个有字母和数字以及空格组成的字符串，和一个字符，
然后输出输入字符串中含有该字符的个数。不区分大小写。
"""


class Solution(object):
    def count_char(self, s, c):
        return s.count(c)


def main():
    print Solution().count_char(raw_input(), raw_input())


if __name__ == '__main__':
    main()
