# coding=utf-8
"""
迷宫问题

定义一个二维数组N*M（其中2<=N<=10;2<=M<=10），如5 × 5数组下所示：

int maze[5][5] = {

        0, 1, 0, 0, 0,

        0, 1, 0, 1, 0,

        0, 0, 0, 0, 0,

        0, 1, 1, 1, 0,

        0, 0, 0, 1, 0,

};

它表示一个迷宫，其中的1表示墙壁，0表示可以走的路，只能横着走或竖着走，不能斜着走，要求编程序找出从左上角到右下角的最短路线。
入口点为[0,0],既第一空格是可以走的路。
6 5
0 1 0 0 0
0 1 0 1 0
0 0 0 1 0
0 1 1 1 0
0 1 0 0 0
0 0 0 1 0

这个题用DFS求解即可

千万注意, 在求解DFS的时候, temp路径和visited数组一定要成对更新
在刚开始设置为True的时候, 一定要在出口出将其设置为False, 路径要在出口出pop
"""


class Solution(object):
    def dfs(self, graph, n, m, i, j, visited, temp, res):
        """
        :type graph: list[list[bool]]
        :type n: int
        :type m: int
        :type i: int
        :type j: int
        :type visited: list[list[bool]]
        :type temp: list[Tuple]
        :type res: list[Tuple]
        """
        temp.append((i, j))
        visited[i][j] = True
        if i == n - 1 and j == m - 1:
            if not res or len(temp) < len(res):
                res[:] = temp
                visited[i][j] = False  # Remember to set False when exit
                temp.pop()
                return
        if j < m - 1 and not visited[i][j + 1] and graph[i][j + 1]:
            self.dfs(graph, n, m, i, j + 1, visited, temp, res)
        if i < n - 1 and not visited[i + 1][j] and graph[i + 1][j]:
            self.dfs(graph, n, m, i + 1, j, visited, temp, res)
        if i > 0 and not visited[i - 1][j] and graph[i - 1][j]:
            self.dfs(graph, n, m, i - 1, j, visited, temp, res)
        if j > 0 and not visited[i][j - 1] and graph[i][j - 1]:
            self.dfs(graph, n, m, i, j - 1, visited, temp, res)
        visited[i][j] = False
        temp.pop()


def main():
    n, m = map(int, raw_input().split())
    graph = [map(lambda x: not bool(int(x)), raw_input().split()) for _ in range(n)]
    res = []
    Solution().dfs(graph, n, m, 0, 0, [[False] * m for _ in range(n)], [], res)
    print "\n".join(map(lambda x: "(%d,%d)" % (x[0], x[1]), res))


if __name__ == '__main__':
    main()
