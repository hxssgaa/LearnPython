# coding=utf-8
"""
成绩排序

查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
      都按先录入排列在前的规则处理。

3
0
fang 90
yang 50
ning 70
"""


class Solution(object):
    def sort_data(self, data, type):
        return sorted(data, key=lambda x: x[1], reverse=type == 0)


def main():
    n, type = input(), input()
    data = [raw_input().split() for _ in xrange(n)]
    data = [(d[0], int(d[1])) for d in data]
    print "\n".join("%s %d" % (e[0], e[1]) for e in Solution().sort_data(data, type))


if __name__ == '__main__':
    main()
