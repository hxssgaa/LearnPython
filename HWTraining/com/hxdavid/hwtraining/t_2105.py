# coding=utf-8
"""
蛇形矩阵

题目说明
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。

样例输入
5
样例输出
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""


class Solution(object):
    def get_result(self, n):
        res = []
        for i in range(n):
            s = (i * i + i + 2) // 2
            res.append(" ".join(str((j * j + j + (i + 1) * 2 * j + s * 2) // 2) for j in range(n - i)))
        return "\n".join(res)


def main():
    print Solution().get_result(input())


if __name__ == '__main__':
    main()
