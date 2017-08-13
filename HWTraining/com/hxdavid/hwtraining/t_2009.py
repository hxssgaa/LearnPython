# coding=utf-8
"""
尼科彻斯定理

验证尼科彻斯定理，即：任何一个整数m的立方都可以写成m个连续奇数之和。
例如：
1^3=1
2^3=3+5
3^3=7+9+11
4^3=13+15+17+19
"""


class Solution(object):
    def get_seque_odd_num(self, m):
        cube = m ** 3
        mid = cube / m
        return range(mid - m + 1, mid + m, 2)


def main():
    print "+".join(map(str, Solution().get_seque_odd_num(input())))


if __name__ == '__main__':
    main()
