# coding=utf-8
"""
24点运算

计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，本问题中，
扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王：
                   3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。
详细说明：
1.运算只考虑加减乘除运算，没有阶乘等特殊运算符号，友情提醒，整数除法要当心；
2.牌面2~10对应的权值为2~10, J、Q、K、A权值分别为为11、12、13、1；
3.输入4张牌为字符串形式，以一个空格隔开，首尾无空格；如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
4.输出的算式格式为4张牌通过+-*/四个运算符相连，中间无空格，4张牌出现顺序任意，只要结果正确；
5.输出算式的运算顺序从左至右，不包含括号，如1+2+3*4的结果为24
6.如果存在多种算式都能计算得出24，只需输出一种即可，如果无法得出24，则输出“NONE”表示无解。

解题思路:
这个题无需理会, 因为答案不唯一, OJ无法判断正确与否
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

    def solve_24_point(self, card, show_process=True):
        if not card:
            return False
        card.sort()
        res = []
        solved = self.solve_24_point_helper(card, [False] * len(card), 0, [], res)
        if show_process and solved:
            type_map = {0: '+', 1: '-', 2: '*', 3: '/'}
            vec = ['J', 'Q', 'K']

            def card_map(x):
                return {
                           11: 'J',
                           12: 'Q',
                           13: 'K',
                           1: 'A',
                       }.get(x) or str(int(x))

            print "%s%s" % (card_map(res[0][1]), "".join(map(lambda x: "%s%s" % (type_map[x[0]], card_map(x[1])),
                                                             res[1:])))
        return solved


def main():
    def card_map(x):
        return {
                   'J': 11.0,
                   'Q': 12.0,
                   'K': 13.0,
                   'A': 1.0,
               }.get(x) or float(x)

    try:
        if not Solution().solve_24_point(map(card_map, raw_input().split()), True):
            print 'NONE'
    except ValueError:
        print 'NONE'


if __name__ == '__main__':
    main()
