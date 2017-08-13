# coding=utf-8
"""
求int型数据在内存中存储时1的个数


输入一个int型数据，计算出该int型数据在内存中存储时1的个数。
这个题注意的是bin的用法
真正32位2进制表示方法如下:

'{:32b}'.format(n & 0xffffffff)
"""


class Solution(object):
    def count_binary_one(self, n):
        return '{:32b}'.format(n & 0xffffffff).count('1')


def main():
    print Solution().count_binary_one(input())


if __name__ == '__main__':
    main()
