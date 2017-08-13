# coding=utf-8
"""
在字符串中找出连续最长的数字串

输出字符串中最长的数字字符串和它的长度。
如果数字字符串为空，则只输出0
如 input: dadfsaf  output:0
"""
import re


class Solution(object):
    def max_consecutive_numbers(self, s):
        return max(map(lambda x: (len(x), x), re.split('[^0-9]', s)))


def main():
    digit_len, digit_str = Solution().max_consecutive_numbers(raw_input())
    if digit_len == 0:
        print digit_len
    else:
        print "%s,%d" % (digit_str, digit_len)


if __name__ == '__main__':
    main()
