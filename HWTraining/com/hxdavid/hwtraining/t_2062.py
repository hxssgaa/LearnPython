# coding=utf-8
"""
iNOC产品部-杨辉三角的变形

            1
         1  1  1
      1  2  3  2  1
   1  3  6  7  6  3  1
1  4  10 16 19  16 10  4  1
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数，左上角数到右上角的数，3个数之和
（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出3。
"""


class Solution(object):
    def get_value_pascal_triangle(self, n, i):
        if i < 1 or i > 2 * n - 1:
            return 0
        elif i == 1:
            return 1
        return self.get_value_pascal_triangle(n - 1, i - 2) + self.get_value_pascal_triangle(n - 1, i - 1) + \
               self.get_value_pascal_triangle(n - 1, i)

    def first_even_pascal_triangle(self, n):
        for i in range(1, n + 1):
            if self.get_value_pascal_triangle(n, i) % 2 == 0:
                return i
        return -1


def main():
    print Solution().first_even_pascal_triangle(input())


if __name__ == '__main__':
    main()