# coding=utf-8
"""
Redraiment的走法

样例输入
6
2 5 1 5 4 5

样例输出
3

提示
Example:
6个点的高度各为 2 5 1 5 4 5
如从第1格开始走,最多为3步, 2 4 5
从第2格开始走,最多只有1步,5
而从第3格开始走最多有3步,1 4 5
从第5格开始走最多有2步,4 5
所以这个结果是3。

直接LIS求解即可
注意lis[i]是以i为终点的及S0...SI的最长递增子序列
也就是说最终最长递增子序列等于max(lis)

"""


class Solution(object):
    def longest_increasing_sequence(self, seq):
        n = len(seq)
        lis = [1] * n
        for i in xrange(1, n):
            for j in xrange(0, i):
                if seq[j] < seq[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
        return max(lis)


def main():
    n = input()
    seq = [input() for _ in xrange(n)]
    print Solution().longest_increasing_sequence(seq)


if __name__ == '__main__':
    main()
