# coding=utf-8
"""
自守数

自守数是指一个数的平方的尾数等于该数自身的自然数。例如：252 = 625，762 = 5776，93762 = 87909376。请求出n以内的自守数的个数
"""


class Solution(object):
    def calc_auto_morphic_numbers(self, n):
        return len(filter(lambda i: str(i ** 2)[-(len(str(i))):] == str(i), range(0, n + 1)))


def main():
    print Solution().calc_auto_morphic_numbers(input())


if __name__ == '__main__':
    main()
