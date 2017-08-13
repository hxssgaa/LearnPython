# coding=utf-8
"""
笔画

一笔画游戏是一个数学游戏  即平面上由多条线段构成的一个图形能不能一笔画成，使得在每条线段上都不重复？例如汉字‘日’和‘中’字都可以一笔画的，而‘田’和‘目’则不能。

请编程实现一笔画：
首先输入坐标系上的点数个数，然后输入点的坐标，请判断这张图是否可以一笔画出，并输出画线顺序 （每条线段必须经过一次，且只能经过一次。每个端点可以经过多次。）
当有多种方式可以完成一笔画时，每一步都必须尽可能先画数值最小的端点。
如  输入 1,2  1,3 2，3 三个点

画线顺序为：1 2 3 1
如果能画线输出true
其他输出false；

这个题输入的是边(点1,点2), 点的个数为输入的点的最大数.
这个题其实就是考察半欧拉图的判断, 首先要知道以下概念:

欧拉环：图中经过每条边一次且仅一次的环；
欧拉路径：图中经过每条边一次且仅一次的路径；
欧拉图：有至少一个欧拉环的图；
半欧拉图：没有欧拉环，但有至少一条欧拉路径的图。

一个无向图是欧拉图当且仅当该图是连通的且所有点的度数都是偶数
一个无向图是半欧拉图当且仅当该图是连通的且有且只有2个点的度数是奇数

同时注意一个无向图是否连通的判断:
其实就是通过DFS去看是否最终所有的节点都能visit一遍.
"""


class Solution(object):
    def is_connected_graph_helper(self, i, n, graph, visited):
        if all(visited):
            return True
        for node in range(1, n + 1):
            if not visited[node] and graph[i][node]:
                visited[node] = True
                if self.is_connected_graph_helper(node, n, graph, visited):
                    return True
                visited[node] = False
        return False

    def is_connected_graph(self, n, graph):
        """
        :type n: int
        :type graph: list[list[int]]
        :rtype: bool
        """
        return self.is_connected_graph_helper(1, n, graph, [True] * 2 + [False] * (n - 1))

    def is_half_euler_graph(self, n, graph):
        """
        :type n: int
        :type graph: list[list[int]]
        :rtype: bool
        """
        if not self.is_connected_graph(n, graph):
            return False
        odd = sum(sum(graph[i]) % 2 != 0 for i in range(1, n + 1))
        return odd == 0 or odd == 2


def main():
    ps = []
    n = input()
    for i in range(n):
        ps.append(map(int, raw_input().split()))
    n = max(max(e) for e in ps)
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for e in ps:
        graph[e[0]][e[1]] = graph[e[1]][e[0]] = True
    print "true" if Solution().is_half_euler_graph(n, graph) else "false"


if __name__ == '__main__':
    main()
