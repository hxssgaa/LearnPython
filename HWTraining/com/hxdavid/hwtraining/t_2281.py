# coding=utf-8
"""
扑克牌大小

扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A、2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）：
3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如：4 4 4 4-joker JOKER。
请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR。
基本规则：
（1）输入每手牌可能是个子、对子、顺子（连续5张）、三个、炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
（2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）；
（3）大小规则跟大家平时了解的常见规则相同，个子、对子、三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
（4）输入的两手牌不会出现相等的情况。

此题学会几个套路:
- 首先是判断是否列表所有元素相等可以用这个办法:
res_bool = all(x==l[0] for x in l)

- 然后对于switch在Python中可以用这个套路:
return {'a': 1,
        'b': 2,
        ...
        'z': 26,
        }.get(e) or xxx
使用or而非get(e,default_val)的好处在于执行xxx可以用异常捕获,否则default_val可能会发生异常,导致判断逻辑错误.

"""


class Solution(object):
    def get_poker_kind(self, poker):
        """
        :type poker: list[str]
        :return: int
        """
        is_poker_equal = all(x == poker[0] for x in poker)
        if is_poker_equal:
            return len(poker)
        if len(poker) > 2:
            return 5
        for p in poker:
            if p == 'joker' or p == 'JOKER':
                return 6
        return 5

    def get_card_order(self, card):
        try:
            return {'J': 9,
                    'Q': 10,
                    'K': 11,
                    'A': 12,
                    '2': 13,
                    'joker': 14,
                    'JOKER': 15,
                    }.get(card) or int(card) - 2
        except ValueError:
            return 0

    def compare_poker(self, pokers):
        """
        :type pokers: list[str]
        :rtype: str
        """
        max_poker = pokers[0].split()
        max_kind = self.get_poker_kind(max_poker)
        for i in range(1, len(pokers)):
            poker = pokers[i].split()
            kind = self.get_poker_kind(poker)
            if kind == 6 or max_kind == 6:
                return "joker JOKER"
            if max_kind != kind and kind != 4 and max_kind != 4:
                return "ERROR"
            if max_kind != kind and kind == 4:
                max_kind = kind
                max_poker = poker
            elif max_kind == kind and self.get_card_order(poker[0]) > self.get_card_order(max_poker[0]):
                max_kind = kind
                max_poker = poker
        return " ".join(max_poker)


def main():
    print Solution().compare_poker(raw_input().split('-'))


if __name__ == '__main__':
    main()
