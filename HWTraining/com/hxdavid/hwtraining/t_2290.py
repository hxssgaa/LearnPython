# coding=utf-8
"""
字符串最后一个单词的长度

计算字符串最后一个单词的长度，单词以空格隔开。
"""


class Solution(object):
    @staticmethod
    def length_of_last_word():
        input_str = raw_input("")
        str_len = 0
        for c in reversed(input_str):
            if c == ' ':
                break
            str_len += 1
        print str_len


if __name__ == '__main__':
    Solution.length_of_last_word()
