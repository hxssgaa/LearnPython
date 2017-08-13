# coding=utf-8
"""
字符统计

如果统计的个数相同，则按照ASII码由小到大排序输出 。如果有其他字符，则对这些字符不用进行统计。
实现以下接口：
    输入一个字符串，对字符中的各个英文字符，数字，空格进行统计（可反复调用）
    按照统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASII码由小到大排序输出
    清空目前的统计结果，重新统计
调用者会保证：
输入的字符串以‘\0’结尾。
"""
from collections import defaultdict


class Solution(object):
    def char_occurrences_statistic(self, s):
        m = defaultdict(int)
        for e in s:
            if not e.isalnum() and e != ' ':
                continue
            m[e] += 1
        res = [(v, k) for k, v in m.items()]
        res.sort(key=lambda x: x[1])
        res.sort(key=lambda x: x[0], reverse=True)
        return map(lambda x: x[1], res)


def main():
    print "".join(Solution().char_occurrences_statistic(raw_input()))


if __name__ == '__main__':
    main()
