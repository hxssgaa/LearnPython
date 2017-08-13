# coding=utf-8
"""
字符串匹配

题目标题：
判断短字符串中的所有字符是否在长字符串中全部出现

这个题考察检测subset的判断
在Python中检测set1是否是set2的子集, 就用
set1 < set2就行
"""


class Solution(object):
    def is_all_char_exist(self, short_str, long_str):
        return set(short_str) < set(long_str)


def main():
    print 'true' if Solution().is_all_char_exist(raw_input(), raw_input()) else 'false'


if __name__ == '__main__':
    main()
