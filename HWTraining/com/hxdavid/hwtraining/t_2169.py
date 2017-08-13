# coding=utf-8
"""
数据分类处理

信息社会，有海量的数据需要分析处理，比如公安局分析身份证号码、QQ用户、手机号码、银行帐号等信息及活动记录。
采集输入大数据和分类规则，通过大数据分类处理程序，将大数据分类输出。

15 123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123
5 6 3 6 3 0
"""


class Solution(object):
    def category_big_data(self, i, r):
        """
        :type i: list[int]
        :type r: list[int]
        :rtype: str
        """
        if not i or not r:
            return "0"
        res = []
        i = [(str(i_i), str(e_i)) for i_i, e_i in enumerate(i)]
        for e_r in map(str, sorted(set(r))):
            i_j = filter(lambda x: e_r in x[1], i)
            if not i_j:
                continue
            res.append(e_r)
            res.append(str(len(i_j)))
            for e in i_j:
                res.append(e[0])
                res.append(e[1])
        return "%d %s" % (len(res), " ".join(res))


def main():
    i = raw_input().split()
    r = raw_input().split()
    print Solution().category_big_data(map(int, i[1:]), map(int, r[1:]))


if __name__ == '__main__':
    main()
