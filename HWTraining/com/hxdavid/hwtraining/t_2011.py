# coding=utf-8
"""
公共字串计算

计算两个字符串的最大公共字串的长度，字符不区分大小写
"""


class Solution(object):
    def get_common_str_len(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        dp = [[0] * (n2 + 1) for _ in xrange(n1 + 1)]
        max_len = 0
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    if dp[i + 1][j + 1] > max_len:
                        max_len = dp[i + 1][j + 1]
        return max_len


def main():
    s1, s2 = raw_input().split()
    print Solution().get_common_str_len(s1.lower(), s2.lower())


if __name__ == '__main__':
    main()
