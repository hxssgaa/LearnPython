# coding=utf-8
"""
字符串通配符

问题描述：在计算机中，通配符一种特殊语法，广泛应用于文件搜索、数据库、正则表达式等领域。现要求各位实现字符串通配符的算法。
要求：
实现如下2个通配符：
*：匹配0个或以上的字符（字符由英文字母和数字0-9组成，不区分大小写。下同）
？：匹配1个字符

abcdefzzz   abcdef*
"""
import re


class Solution(object):
    def is_match(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n, m = len(s), len(p)
        dp = [[False for _ in xrange(m + 1)] for _ in xrange(n + 1)]  # Learn to define matrix in correct (n, m) order.
        # If p and s is both empty, we got a match.
        dp[0][0] = True
        for j in range(1, m + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]  # Match 0 or more characters
                elif p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]  # Match 1 character
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[n][m]


def main():
    p, s = raw_input(), raw_input()
    print "true" if Solution().is_match(s.lower(), p.lower()) else "false"


if __name__ == '__main__':
    main()
