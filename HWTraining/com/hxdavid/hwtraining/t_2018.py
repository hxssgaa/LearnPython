# coding=utf-8
"""
百钱买百鸡问题

公元前五世纪，我国古代数学家张丘建在《算经》一书中提出了“百鸡问题”：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
"""


class Solution(object):
    def solve(self):
        res = []
        for z in xrange(3, 100, 3):
            x = (8 * z / 3 - 200) / 2
            y = 100 - x - z
            if x >= 0 and y >= 0 and z >= 0:
                res.append((x, y, z))
        return res


def main():
    _ = input()
    for e in Solution().solve():
        print "%d %d %d" % (e[0], e[1], e[2])


if __name__ == '__main__':
    main()
