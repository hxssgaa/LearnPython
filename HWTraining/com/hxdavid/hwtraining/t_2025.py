# coding=utf-8
"""
矩阵乘法

直接求解矩阵乘法的结果就行

2
2
2
3 8
8 0
9 0
18 9
"""


class Solution(object):
    def matrix_multi(self, mat1, mat2):
        if not mat1 or not mat2 or not mat1[0] or not mat2[0] or len(mat1[0]) != len(mat2):
            return []
        n, m = len(mat1), len(mat2[0])
        res = [[0] * m for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                res[i][j] = sum(mat1[i][x] * mat2[x][j] for x in xrange(len(mat1[0])))
        return res


def main():
    n1 = input()
    mid = input()
    m2 = input()
    mat1 = [map(int, raw_input().split()) for _ in xrange(n1)]
    mat2 = [map(int, raw_input().split()) for _ in xrange(mid)]
    res = Solution().matrix_multi(mat1, mat2)
    for l in res:
        print " ".join(map(str, l))


if __name__ == '__main__':
    main()
