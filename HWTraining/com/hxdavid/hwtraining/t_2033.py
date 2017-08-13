# coding=utf-8
"""
24点游戏算法

问题描述：给出4个1-10的数字，通过加减乘除，得到数字为24就算胜利
输入：
4个1-10的数字。[数字允许重复，测试用例保证无异常数字]
输出：
true or false

这个题我只用了第一种手段, 也就是直接DFS顺序求解的方法, 只适用于四个数连续相加,减,乘,除
但是对于(1+2)*(2+6), 这样用括号的手段未做考虑, 因此此题可以考虑用排列组合的方式和添加括号的方式求解该题.
"""


class Solution(object):
    def solve_24_point_helper(self, card, visited, temp, path, res):
        if all(visited) and temp == 24:
            res[:] = path
            return True
        for i in xrange(0, len(card)):
            if not visited[i]:
                visited[i] = True
                if temp == 0 and self.solve_24_point_helper(card, visited, card[i], path + [(0, card[i])], res):
                    return True
                if temp != 0 and \
                        (self.solve_24_point_helper(card, visited, temp + card[i], path + [(0, card[i])], res) or
                             self.solve_24_point_helper(card, visited, temp - card[i], path + [(1, card[i])], res) or
                             self.solve_24_point_helper(card, visited, temp * card[i], path + [(2, card[i])], res) or
                             self.solve_24_point_helper(card, visited, temp / card[i], path + [(3, card[i])], res)):
                    return True
                visited[i] = False
        return False

    def solve_24_point(self, card, show_process=False):
        if not card:
            return False
        card.sort()
        res = []
        solved = self.solve_24_point_helper(card, [False] * len(card), 0, [], res)
        if show_process and solved:
            type_map = {0: '+', 1: '-', 2: '*', 3: '/'}
            print "%d%s" % (res[0][1], "".join(map(lambda x: "%s%d" % (type_map[x[0]], x[1]), res[1:])))
        return solved


def main():
    print "true" if Solution().solve_24_point(map(float, raw_input().split()), True) else "false"


if __name__ == '__main__':
    main()
