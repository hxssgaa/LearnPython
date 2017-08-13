# coding=utf-8
"""
求小球落地5次后所经历的路程和第5次反弹的高度

假设一个球从任意高度自由落下，每次落地后反跳回原高度的一半; 再落下, 求它在第5次落地时，共经历多少米?第5次反弹多高？
"""


class Solution(object):
    def get_journey(self, high):
        return 23.0 / 8 * high

    def get_bounce_high(self, high):
        return high / 32.0


def main():
    n = input()
    print Solution().get_journey(n)
    print Solution().get_bounce_high(n)


if __name__ == '__main__':
    main()
