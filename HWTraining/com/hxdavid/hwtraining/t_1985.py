# coding=utf-8
"""
人民币转换

考试题目和要点：
1、中文大写金额数字前应标明“人民币”字样。中文大写金额数字应用壹、贰、叁、肆、伍、陆、柒、捌、玖、拾、佰、仟、万、亿、元、角、分、零、
整等字样填写。（30分）
2、中文大写金额数字到“元”为止的，在“元”之后，应写“整字，如￥ 532.00应写成“人民币伍佰叁拾贰元整”。在”角“和”分“后面不写”整字。（30分）
3、阿拉伯数字中间有“0”时，中文大写要写“零”字，阿拉伯数字中间连续有几个“0”时，中文大写金额中间只写一个“零”字，如￥6007.14，应写成“人民
币陆仟零柒元壹角肆分“。

解题思路
这个题比较复杂, 但是分解成亿和万就不会有问题, 因为它会分解到千, 千的时候特殊处理多0, 十的情况即可

这个题真正注意的点是在Python如何使用字符串拼接

这里强烈推荐用数组[]的方式进行拼接, 首先速度快, 其次它可以处理中文, 因为str会涉及到中文str[0]变成单个字符的问题, 而数组却不会.
"""


class Solution(object):
    DIGIT_MAP = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
    HIGH_DIGIT_MAP = ['仟', '佰', '拾']

    #  10001
    #  1000
    #  10007
    #   0007
    def convert_to_rmb_int_helper(self, num):
        if num == '0':
            return self.DIGIT_MAP[0]
        if len(num) >= 9:
            return '%s亿%s' % (self.convert_to_rmb_int_helper(num[:-8]), self.convert_to_rmb_int_helper(num[-8:]))
        elif len(num) >= 5:
            return '%s万%s' % (self.convert_to_rmb_int_helper(num[:-4]), self.convert_to_rmb_int_helper(num[-4:]))
        zero_read = False
        res = []
        for i, digit in enumerate(num):
            if digit == '0' and not zero_read:
                res.append(self.DIGIT_MAP[0])
                zero_read = True
            elif digit != '0':
                offset = i + 4 - len(num)
                if offset != 2 or int(digit) != 1:
                    res.append(self.DIGIT_MAP[int(digit)])
                if offset < len(self.HIGH_DIGIT_MAP):
                    res.append(self.HIGH_DIGIT_MAP[offset])
        if res[-1] == self.DIGIT_MAP[0]:
            del res[-1]
        return "".join(res)

    def convert_to_rmb_decimal_helper(self, num):
        if not num:
            return '整'
        if len(num) == 1:
            num += '0'
        num = num[:2]
        if all(map(lambda x: x == '0', num)):
            return '整'
        return '%s%s' % (self.DIGIT_MAP[0] if num[0] == '0' else self.DIGIT_MAP[int(num[0])] + '角',
                         '' if num[1] == '0' else self.DIGIT_MAP[int(num[1])] + '分')

    def convert_to_rmb(self, num):
        if '.' not in num:
            num += '.00'
        int_part, decimal_part = num.split('.')
        return "人民币%s元%s" % \
               (self.convert_to_rmb_int_helper(str(int(int_part))), self.convert_to_rmb_decimal_helper(decimal_part))


def main():
    print Solution().convert_to_rmb(raw_input())


if __name__ == '__main__':
    main()
