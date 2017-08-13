# coding=utf-8
"""
表示数字

将一个字符中所有出现的数字前后加上符号“*”，其他字符保持不变

这个题要记住正则表达式的re.sub用法
对于repl字符串可以用lambda的形式来表示, 如下

    re.sub(r'\d+', lambda x: '*%s*' % x.group(), s)   # 将所有的数字加上星号

"""
import re


class Solution(object):
    def mark_num(self, s):
        return re.sub(r'\d+', lambda x: '*%s*' % x.group(), s)


def main():
    print Solution().mark_num(raw_input())


if __name__ == '__main__':
    main()
