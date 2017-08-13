# coding=utf-8
"""
字符串排序

编写一个程序，将输入字符串中的字符按如下规则排序。
规则1：英文字母从A到Z排列，不区分大小写。
      如，输入：Type 输出：epTy
规则2：同一个英文字母的大小写同时存在时，按照输入顺序排列。
    如，输入：BabA 输出：aABb
规则3：非英文字母的其它字符保持原来的位置。
    如，输入：By?e 输出：Be?y
样例：
    输入：
   A Famous Saying: Much Ado About Nothing(2012/8).
    输出：
   A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8).

"""


class Solution(object):
    def sort_str(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = sorted(filter(lambda x: ('a' <= x <= 'z') or ('A' <= x <= 'Z'), s), key=lambda x: x.lower())
        l = list(s)
        cur = 0
        for i, e in enumerate(l):
            if ('a' <= e <= 'z') or ('A' <= e <= 'Z'):
                l[i] = r[cur]
                cur += 1
        return "".join(l)


def main():
    print Solution().sort_str(raw_input())


if __name__ == '__main__':
    main()
