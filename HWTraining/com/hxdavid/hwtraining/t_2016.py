# coding=utf-8
"""
计算日期到天数转换

描述
根据输入的日期，计算是这一年的第几天。。
详细描述：
输入某年某月某日，判断这一天是这一年的第几天？。
"""
from datetime import datetime


class Solution(object):
    def count_day_of_year(self, y, m, d):
        return (datetime(y, m, d) - datetime(y, 1, 1)).days + 1


def main():
    year, month, day = input(), input(), input()
    print(Solution().count_day_of_year(year, month, day))


if __name__ == '__main__':
    main()
