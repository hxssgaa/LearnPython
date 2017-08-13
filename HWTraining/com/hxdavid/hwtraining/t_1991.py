# coding=utf-8
"""
棋盘格子走法

请编写一个函数（允许增加子函数），计算n x m的棋盘格子（n为横向的格子数，m为竖向的格子数）
沿着各自边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
"""


class Solution(object):
    def count_grid_ways(self, n, m):
        if n == 0 and m == 0:
            return 0
        elif n == 1:
            return m + 1
        elif m == 1:
            return n + 1
        return self.count_grid_ways(n - 1, m) + self.count_grid_ways(n, m - 1)


def main():
    print Solution().count_grid_ways(input(), input())


if __name__ == '__main__':
    main()
