# coding=utf-8
"""
句子逆序

将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符
"""


class Solution(object):
    def reverse_sentence(self, s):
        return ' '.join(reversed(s.split()))


def main():
    print Solution().reverse_sentence(raw_input())


if __name__ == '__main__':
    main()
