# coding=utf-8
"""
等差数列

功能:等差数列 2，5，8，11，14。。。。
输入:正整数N >0
输出:求等差数列前N项和
返回:转换成功返回 0 ,非法输入与异常返回-1
"""


class Solution(object):
    def sn(self, n):
        a1, d = 2, 3
        return a1 * n + n * (n - 1) * d // 2


def main():
    print Solution().sn(input())


if __name__ == '__main__':
    main()
