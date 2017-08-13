# coding=utf-8
"""
合并表记录

数据表记录包含表索引和数值。请对表索引相同的记录进行合并，合并后表记录为相同索引表的数值求和

"""
from collections import OrderedDict


class Solution(object):
    def merge_data(self, data):
        m = OrderedDict()
        for k, v in data:
            if k not in m:
                m[k] = v
            else:
                m[k] += v
        return '\n'.join('%d\n%d' % (k, v) for k, v in m.items())


def main():
    n = input()
    data = [(input(), input()) for _ in xrange(n)]
    print Solution().merge_data(data)


if __name__ == '__main__':
    main()
