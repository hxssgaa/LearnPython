# coding=utf-8
"""
查找两个字符串a,b中的最长公共子串

这个题为LCS题目的变种:
首先回顾一下基础Longest Common Sequence(中间允许元素可以不连续)的解法
如果s1:abcxdef, s2:bcdef, 那么LCS的结果是5

解法:
    def longest_common_subsequence(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in xrange(n1 + 1)]
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[n1][n2]

那么对于不允许中间有相隔元素的变种Longest Common Substring的解法:
如果s1:abcxdef, s2:bcdef, 那么LCS的结果是3.
我们令dp[i][j]表示分别以i和j结尾的s1和s2结果子串的最大长度.
我们可以知道当c1==c2的时候dp[i][j] = dp[i-1][j-1]+1
而当c1!=c2的时候那么当前一定不是结果集, 因此dp[i][j]=0
因此我们只需要搜索一遍, 结果集合, 寻找最长的结果子串即为所求.
(注意, 之所以子串s1: abcx, s2: bcd的dp[i][j]为0是因为这里dp定义成结果为i和j的子串. 而很明显c1!=c2时候一定不为结果子串, 所以为0)

解法:
    def longest_common_substring(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in xrange(n1 + 1)]
        max_len = res_end = 0
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > max_len:
                        max_len = dp[i + 1][j + 1]
                        res_end = i + 1
        return s1[res_end - max_len: res_end]

算法非常经典, 一定要牢记.
"""


class Solution(object):
    def longest_common_subsequence(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in xrange(n1 + 1)]
        path = [[(0, 0)] * (n2 + 1) for _ in xrange(n1 + 1)]
        res = []
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    path[i + 1][j + 1] = (i, j)
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
                    if dp[i + 1][j + 1] == dp[i][j + 1]:
                        path[i + 1][j + 1] = (i, j + 1)
                    else:
                        path[i + 1][j + 1] = (i + 1, j)
        i, j = len(s1), len(s2)
        while i > 0 or j > 0:
            x = path[i][j]
            if x[0] == i - 1 and x[1] == j - 1:
                res.insert(0, s1[i - 1])
                i -= 1
                j -= 1
            elif x[0] == i - 1:
                i -= 1
            else:
                j -= 1
        return "".join(res)

    def longest_common_substring(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in xrange(n1 + 1)]
        max_len = res_end = 0
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > max_len:
                        max_len = dp[i + 1][j + 1]
                        res_end = i + 1
        return s1[res_end - max_len: res_end]


def main():
    print Solution().longest_common_subsequence(raw_input(), raw_input())


if __name__ == '__main__':
    main()
