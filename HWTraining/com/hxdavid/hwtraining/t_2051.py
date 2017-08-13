# coding=utf-8
"""
输入n个整数，输出其中最小的k个

描述
输入n个整数，输出其中最小的k个。
"""
from heapq import heappush, heappop


class Solution(object):
    def k_min_elements(self, data, k):
        heap, res = [], []
        for e in data:
            heappush(heap, e)
        while heap and k > 0:
            res.append(heappop(heap))
            k -= 1
        return res


def main():
    n, k = map(int, raw_input().split())
    data = map(int, raw_input().split())
    print " ".join(map(str, Solution().k_min_elements(data, k)))


if __name__ == '__main__':
    main()
