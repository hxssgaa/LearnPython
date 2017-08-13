# coding=utf-8
"""
（练习用）挑7

输出7有关数字的个数，包括7的倍数，还有包含7的数字（如17，27，37...70，71，72，73...）的个数
"""


class Solution(object):
    @staticmethod
    def pick_seven(n):
        res = 0
        for i in range(7, n + 1):
            if '7' in str(i) or i % 7 == 0:
                res += 1
        return res


def main():
    print Solution.pick_seven(input())


if __name__ == '__main__':
    main()
