# coding=utf-8
"""
整形数组合并

题目标题：
将两个整型数组按照升序合并，并且过滤掉重复数组元素

3
1 2 5
4
-1 0 3 2
"""


class Solution(object):
    def merge_array(self, d1, d2):
        return sorted(set(d1 + d2))


def main():
    n1 = input()
    d1 = map(int, raw_input().split())
    n2 = input()
    d2 = map(int, raw_input().split())
    print "".join(map(str, Solution().merge_array(d1, d2)))


if __name__ == '__main__':
    main()
