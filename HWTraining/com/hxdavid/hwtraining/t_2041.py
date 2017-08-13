# coding=utf-8
"""
放苹果

题目描述
把M个同样的苹果放在N个同样的盘子里，允许有的盘子空着不放，问共有多少种不同的分法？（用K表示）5，1，1和1，5，1 是同一种分法。

输入
每个用例包含二个整数M和N。0<=m<=10，1<=n<=10。<=n<=10<=m<=10

样例输入
7 3

样例输出
8

这个题考察动态规划.
实际上对于f(m,n), 假如m >= n 的情况下:
f(m,n) = f(m-n,n) + f(m,n-1)
这是因为只有两种分法, 一种是每个盘子中都放一个苹果, 要么就是其中一个盘子的苹果是空的, 因为如果后者其中一个盘子苹果不为空, 那么一定
是属于前者情况.

而只有一个盘子或者苹果数为0的情况的话, 只有一种为空的分法
"""


class Solution(object):
    def count_apple(self, m, n):
        if m < 0:
            return 0
        if m == 0 or n == 1:
            return 1
        return self.count_apple(m - n, n) + self.count_apple(m, n - 1)


def main():
    m, n = map(int, raw_input().split())
    print Solution().count_apple(m, n)


if __name__ == '__main__':
    main()
