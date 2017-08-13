# coding=utf-8
"""
【中级】字符串运用-密码截取

题目描述:

Catcher是MCA国的情报员，他工作时发现敌国会用一些对称的密码进行通信，比如像这些ABBA，ABA，A，123321，
但是他们有时会在开始或结束时加入一些无关的字符以防止别国破解。比如进行下列变化 ABBA->12ABBA,ABA->ABAKK,
123321->51233214　。因为截获的串太长了，而且存在多种可能的情况（abaaab可看作是aba,或baaab的加密形式），
Cathcer的工作量实在是太大了，他只能向电脑高手求助，你能帮Catcher找出最长的有效密码串吗？

这个题实际上就是求最大回文子串
这个题的解法实际上就是利用 two-pointers. (j, k)围绕中心点i不断延展, 从0到n-1不但遍历i
从i = [0, n)开始
令j = k = i, 并且如果s[k + 1] == s[k]的情况下不断让k加1
然后令 i = k + 1
然后通过j和k不断向左右延伸, 直到s[j - 1] != s[k + 1]为止
当 (n - i) <= max_len // 2的时候需要停止循环, 因为此时再判断没有意义了
这样的话记录start和max_len的信息, 从而求得最大回文子串.
"""


class Solution(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n, max_len, start = 0, len(s), 1, 0
        if not s or n == 0 or n == 1:
            return s
        while i < n:
            if n - i <= max_len // 2:
                break
            j = k = i
            while k < n - 1 and s[k] == s[k + 1]:
                k += 1
            i = k + 1
            while k < n - 1 and j > 0 and s[k + 1] == s[j - 1]:
                k += 1
                j -= 1
            if k - j + 1 > max_len:
                start = j
                max_len = k - j + 1
        return s[start:start + max_len]


def main():
    print len(Solution().longest_palindrome(raw_input()))


if __name__ == '__main__':
    main()
