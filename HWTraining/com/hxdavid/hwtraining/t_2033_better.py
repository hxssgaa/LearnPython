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
    def solve_24_point_helper(self, card, visited, path, res):
        if all(visited):
            res.append(''.join(path))
            res.append('(%s)' % res[-1].replace('*', ')*(').replace('/', ')/('))
            return
        for i in xrange(len(card)):
            if visited[i]:
                continue
            visited[i] = True
            if all(visited):
                self.solve_24_point_helper(card, visited, path + [str(float(card[i]))], res)
            else:
                for op in '+-*/':
                    self.solve_24_point_helper(card, visited, path + [str(float(card[i]))] + [op], res)
            visited[i] = False

    def solve_24_point(self, card, show_process=False):
        if not card:
            return False
        card.sort()
        res = []
        self.solve_24_point_helper(card, [False] * len(card), [], res)
        for e in res:
            try:
                if eval(e) == 24:
                    if show_process:
                        print e
                    return True
            except ZeroDivisionError:
                continue
        return False


def main():
    print 'true' if Solution().solve_24_point(raw_input().split(), True) else 'false'


if __name__ == '__main__':
    main()
