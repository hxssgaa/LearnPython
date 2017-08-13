# coding=utf-8
"""
字符串分割

连续输入字符串(输出次数为N,字符串长度小于100)，请按长度为8拆分每个字符串后输出到新的字符串数组，
长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
首先输入一个整数，为要输入的字符串个数。
"""


class Solution(object):
    def split_str(self, s):
        if len(s) > 8:
            return '%s\n%s' % (self.split_str(s[:8]), self.split_str(s[8:]))
        return ''.join(reversed(''.join(reversed(s)).zfill(8)))


def main():
    n = input()
    print '\n'.join(Solution().split_str(raw_input()) for _ in xrange(n))


if __name__ == '__main__':
    main()
