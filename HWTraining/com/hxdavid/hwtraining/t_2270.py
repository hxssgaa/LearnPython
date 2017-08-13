# coding=utf-8
"""
删除字符串中出现次数最少的字符

实现删除字符串中出现次数最少的字符，若多个字符出现次数一样，则都删除。输出删除这些单词后的字符串，
字符串中其它字符保持原来的顺序。

注意事项
学会filter的使用可以取出前几个最小的相同的元素.
"""
from collections import defaultdict


class Solution(object):
    def del_least_occurrences(self, s):
        o_map = defaultdict(int)
        for e in s:
            o_map[e] += 1
        min_val = min(o_map.values())
        del_chars = filter(lambda x: o_map[x] == min_val, o_map.keys())
        return "".join(filter(lambda x: x not in del_chars, s))


def main():
    print Solution().del_least_occurrences(raw_input())


if __name__ == '__main__':
    main()
