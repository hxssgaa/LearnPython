# coding=utf-8
"""
统计大写字母个数

找出给定字符串中大写字符(即'A'-'Z')的个数
接口说明
    原型：int CalcCapital(String str);
    返回值：int
"""


class Solution(object):
    def count_capital_str(self, s):
        return len(filter(lambda x: 'A' <= x <= 'Z', s))


def main():
    print Solution().count_capital_str(raw_input())


if __name__ == '__main__':
    main()
