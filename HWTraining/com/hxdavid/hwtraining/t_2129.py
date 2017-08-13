# coding=utf-8
"""
素数伴侣

题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N
（N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到
一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。
输入:
有一个正偶数N（N≤100），表示待挑选的自然数的个数。后面给出具体的数字，范围为[2,30000]。
输出:
输出一个整数K，表示你求得的“最佳方案”组成“素数伴侣”的对数。

这个题解法需要用到 二分图, 这是一个二分图的最大匹配问题.

二分图概念:
设G=(V,E)是一个无向图，如果顶点V可分割为两个互不相交的子集(A,B)，
并且图中的每条边（i，j）所关联的两个顶点i和j分别属于这两个不同的顶点集(i in A,j in B)，
则称图G为一个二分图。

二分图的最大匹配:
给定一个二分图G，在G的一个子图M中，M的边集中的任意两条边都不依附于同一个顶点，则称M是一个匹配.
选择这样的边数最大的子集称为图的最大匹配问题（maximal matching problem)

此处考虑到我们需要将题目中给出的数分成两组, 怎么分呢?
考虑到 奇数+奇数 或者 偶数+偶数 % 2 == 0 一定不是素数.
因此素数一定是 奇数+偶数的组合, 因此我们可以将给出的数分成奇数与偶数两组, 并建立二分图, 并求出二分图的最大匹配.

对于这个题而言, 首先是要学会二分图的建立, 二分图即使是无向图的情况下, 也只需要建立单边
比如 1-2 相连, 则graph[1][2] = True即可, 不需要graph[1][2] = graph[2][1] = True
再建立完了二分图之后, 需要求解二分图最大匹配
二分图最大匹配求解过程:
首先遍历所有的节点, 从该节点开始, 去不断地寻找增广轨.
我们可以用一个link数组去存放某个节点连接的另一个节点是谁
只要找到了link[i]==-1或者往link[i]去搜索也能成功的情况下,那么就算找到了增广轨.同时记录link[i]=s

搜索算法如下:
    def dfs(self, graph, s, visited, link):
        m = len(graph[0])
        for i in range(0, m):
            if graph[s][i] and not visited[i]:
                visited[i] = True
                if link[i] == -1 or self.dfs(graph, link[i], visited, link):
                    link[i] = s
                    return True
        return False

那么实际上二分图的最大匹配的结果,就是不断搜索之后成功的节点个数. 代码如下:
    def max_matching_bio_graph(self, graph):
        if not graph:
            return 0
        n, m = len(graph), len(graph[0])
        link = [-1] * m
        return sum(self.dfs(graph, s, [False] * m, link) for s in range(0, n))

二分图的最大匹配有时候不是那么好理解, 可以记住这些算法, 以备以后需要
注意的是要学会判断以及利用二分图去解决问题, 一般都是那种需要将序列两两配对的情况, 需要求最多的匹配数的情况.

6
6 11 23 25 26 32

"""
import math


class Solution(object):
    def is_prime(self, num):
        if num <= 1:
            return False
        for i in xrange(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def dfs(self, graph, s, visited, link):
        m = len(graph[0])
        for i in range(0, m):
            if graph[s][i] and not visited[i]:
                visited[i] = True
                if link[i] == -1 or self.dfs(graph, link[i], visited, link):
                    link[i] = s
                    return True
        return False

    def max_matching_bio_graph(self, graph):
        """
        :type graph: list[list[int]]
        :rtype: int
        """
        if not graph:
            return 0
        n, m = len(graph), len(graph[0])
        link = [-1] * m  # link[y]记录的是当前与y节点相连的x节点
        return sum(self.dfs(graph, s, [False] * m, link) for s in range(0, n))

    def most_prime_partner(self, nums):
        """
        :type nums: list[int]
        :return: int
        """
        n = len(nums)
        nums = [(i, e) for i, e in enumerate(nums)]
        odds = filter(lambda x: x[1] % 2 == 1, nums)
        evens = filter(lambda x: x[1] % 2 == 0, nums)
        if not odds or not evens:
            return 0
        graph = [[False] * n for _ in range(n)]
        for i, odd in odds:
            for j, even in evens:
                if self.is_prime(odd + even):
                    graph[i][j] = True
        return self.max_matching_bio_graph(graph)


def main():
    n = input()
    if n == 0:
        print 0
        return
    nums = map(int, raw_input().split())
    print Solution().most_prime_partner(nums)


if __name__ == '__main__':
    main()
