# coding=utf-8
"""
求最大连续bit数

功能: 求一个byte数字对应的二进制数字中1的最大连续数，例如3的二进制为00000011，最大连续2个1
输入: 一个byte型的数字
输出: 无
返回: 对应的二进制数字中1的最大连续数
"""


class Solution(object):
    def max_continuous_one(self, num):
        return max(len(e) for e in str(bin(num & 0xff))[2:].zfill(8).split('0'))


def main():
    print Solution().max_continuous_one(input())


if __name__ == '__main__':
    main()
