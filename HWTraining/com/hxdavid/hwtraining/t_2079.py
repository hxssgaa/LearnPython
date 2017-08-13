# coding=utf-8
"""
线性插值

信号测量的结果包括测量编号和测量值。存在信号测量结果丢弃及测量结果重复的情况。

1.测量编号不连续的情况，认为是测量结果丢弃。对应测量结果丢弃的情况，需要进行插值操作以更准确的评估信号。
采用简化的一阶插值方法,由丢失的测量结果两头的测量值算出两者中间的丢失值。
假设第M个测量结果的测量值为A，第N个测量结果的测量值为B。则需要进行(N-M-1)个测量结果的插值处理。
进行一阶线性插值估计的第N+i个测量结果的测量值为A+( (B-A)/(N-M) )*i  (注：N的编号比M大。)
例如：只有测量编号为4的测量结果和测量编号为7的测量结果，测量值分别为4和10
    则需要补充测量编号为5和6的测量结果。
     其中测量编号为5的测量值=4 + ((10-4)/(7-4))*1 = 6
     其中测量编号为6的测量值=4 + ((10-4)/(7-4))*2 = 8

2.测量编号相同，则认为测量结果重复，需要对丢弃后来出现的测量结果。

2 3
4 7
7 10
"""


class Solution(object):
    def linear_interpolation(self, data):
        """
        :type data: list[tuple[int, int]]
        :rtype list[tuple[int, int]]
        """
        res = data[:]
        min_index, max_index = data[0][0], data[-1][0]
        min_val, max_val = data[0][1], data[-1][1]
        data_orders = set(map(lambda x: x[0], data))
        for index in range(min_index + 1, max_index):
            if index in data_orders:
                continue
            res.append((index, int(min_val + (float(max_val - min_val) / (max_index - min_index))
                                   * (index - min_index))))
        res.sort(key=lambda x: x[0])
        return res


def main():
    m, n = map(int, raw_input().split())
    d = []
    used_order = set()
    for _ in range(m):
        t = tuple(map(int, raw_input().split()))
        if t[0] in used_order:
            continue
        d.append(t)
        used_order.add(d[0])
    print "\n".join("%d %d" % (e[0], e[1]) for e in Solution().linear_interpolation(d))


if __name__ == '__main__':
    main()
