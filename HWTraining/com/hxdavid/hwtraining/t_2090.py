# coding=utf-8
"""
学英语

Jessi初学英语，为了快速读出一串数字，编写程序将数字转换成英文：
如22：twenty two，123：one hundred and twenty three。

说明：
数字为正整数，长度不超过十位，不考虑小数，转化结果为英文小写；
输出格式为twenty two；
非法数据请返回“error”；
关键字提示：and，billion，million，thousand，hundred。\

234,123,456,709
20 twenty
two hundred and thirty four billion one hundred and twenty three million four
"""


class Solution(object):
    DIGIT_MAP = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    TEN_DIGIT_MAP = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
                     "eighteen", "nineteen"]
    TEN_DIGIT_ABOVE_MAP = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    HIGH_DIGIT_MAP = ["billion", "million", "thousand"]
    HUNDRED = "hundred"
    AND = "and"

    def spell_digit_below_thousand(self, digit):
        res = []
        if len(digit) == 3 and digit[0] != "0":
            res.append(self.DIGIT_MAP[int(digit[0]) - 1])
            res.append(self.HUNDRED)
            res.append(self.AND)
        if 1 <= len(digit) <= 3 and 10 <= int(digit[-2:]) <= 19:
            res.append(self.TEN_DIGIT_MAP[int(digit[-2:]) - 10])
        else:
            if 2 <= len(digit) <= 3 and digit[-2] != "0":
                res.append(self.TEN_DIGIT_ABOVE_MAP[int(digit[-2]) - 2])
            if 1 <= len(digit) <= 3 and digit[-1] != "0":
                res.append(self.DIGIT_MAP[int(digit[-1]) - 1])
        if not res:
            return ""
        if res[-1] == self.AND:
            res.pop()
        return " ".join(res)

    def spell_digit_eng(self, digit):
        """
        :type digit: str
        :rtype: str
        """
        digit = digit.zfill(12)
        length = len(digit)
        split_digit = list(reversed([digit[length - (i + 1) * 3 if i < 3 else 0: length - i * 3]
                                     for i in range(0, 4)]))
        cur_high_digit = 0
        while split_digit[cur_high_digit] == "000":
            cur_high_digit += 1
        res = []
        for i in xrange(cur_high_digit, len(self.HIGH_DIGIT_MAP)):
            res.append(self.spell_digit_below_thousand(split_digit[i]))
            if not res[-1]:
                res.pop()
                continue
            res.append(self.HIGH_DIGIT_MAP[i])
            if split_digit[i + 1][0] == "0":
                res.append(self.AND)
        res.append(self.spell_digit_below_thousand(split_digit[-1]))
        if not res[-1]:
            res.pop()
        if res and res[-1] == self.AND:
            res.pop()
        return " ".join(res)


def main():
    n = raw_input()
    try:
        ni = int(n)
        if ni <= 0 or len(n) > 10:
            print "error"
            return
        print Solution().spell_digit_eng(n)
    except ValueError:
        print "error"


if __name__ == '__main__':
    main()
