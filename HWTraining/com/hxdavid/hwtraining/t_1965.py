# coding=utf-8
"""
字符逆序

将一个字符串str的内容颠倒过来，并输出。str的长度不超过100个字符。 如：输入“I am a student”，
输出“tneduts a ma I”。


输入参数：
inputString：输入的字符串

返回值：
输出转换好的逆序字符串
"""


class Solution(object):
    def reversed_str(self, s):
        return ''.join(reversed(s))


def main():
    print Solution().reversed_str(raw_input())


if __name__ == '__main__':
    main()
