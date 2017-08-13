# coding=utf-8
"""
记票统计

输入候选人的人数，第二行输入候选人的名字，第三行输入投票人的人数，第四行输入投票。
每行输出候选人的名字和得票数量。

"""
from collections import OrderedDict


class Solution(object):
    def vote_statistic(self, names, vote_names):
        m = OrderedDict((e, 0) for e in names)
        other = 0
        for e in vote_names:
            if e not in m:
                other += 1
            else:
                m[e] += 1
        m['Invalid'] = other
        return m


def main():
    input()
    names = raw_input().split()
    input()
    vote_names = raw_input().split()
    print "\n".join("%s : %d" % (k, v) for k, v in Solution().vote_statistic(names, vote_names).items())


if __name__ == '__main__':
    main()
