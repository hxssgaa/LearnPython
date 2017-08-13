# coding=utf-8
"""
明明的随机数

明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤100），对于其中重复的数字，
只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。
请你协助明明完成“去重”与“排序”的工作。
"""


class Solution(object):
    def process_data(self, data):
        return sorted(set(data))


def main():
    n = input()
    data = [input() for _ in xrange(n)]
    print '\n'.join(map(str, Solution().process_data(data)))


if __name__ == '__main__':
    main()
