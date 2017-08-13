# coding=utf-8
"""
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数

输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数
"""


class Solution(object):
    def statistic_chr(self, s):
        res = [0] * 4
        for c in s:
            if c.isalpha():
                res[0] += 1
            elif c.isspace():
                res[1] += 1
            elif c.isdigit():
                res[2] += 1
            else:
                res[3] += 1
        return "\n".join(map(str, res))


def main():
    print Solution().statistic_chr(raw_input())


if __name__ == '__main__':
    main()
