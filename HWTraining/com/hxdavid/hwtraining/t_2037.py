# coding=utf-8
"""
查找输入整数二进制中1的个数

此题所输入的整数实际上类型是unsigned int.

- 因此本题考察: Python的int和unsigned int类型的转换.
实际上对于整数n就是求n & 0xffffffff即可, 即:
    def uint32(x):
        return x & 0xffffffff

- 那么对于Python的int和C++有符号的int转换如下.
    def int32(x):
        if x > 0xffffffff:
            raise OverflowError
        if x > 0x7fffffff:
            x = int(0x100000000 - x)
            if x < (1 << 31):
                return -x
            else:
                return -(1 << 31)
        return x
"""


class Solution(object):
    def int32(self, x):
        if x > 0xffffffff:
            raise OverflowError
        if x > 0x7fffffff:
            x = int(0x100000000 - x)
            if x < (1 << 31):
                return -x
            else:
                return -(1 << 31)
        return x

    def uint32(self, x):
        return x & 0xffffffff

    def count_binary_one(self, n):
        return str(bin(self.uint32(n))[2:].count("1"))


def main():
    print Solution().int32(1 << 31)
    print Solution().count_binary_one(input())


if __name__ == '__main__':
    main()
