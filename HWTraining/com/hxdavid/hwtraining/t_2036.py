# coding=utf-8
"""
DNA序列

一个DNA序列由A/C/G/T四个字母的排列组合组成。G和C的比例（定义为GC-Ratio）是序列中G和C两个字母的总的出现次数除以总的字母数目（
也就是序列长度）。在基因工程中，这个比例非常重要。因为高的GC-Ratio可能是基因的起始点。
给定一个很长的DNA序列，以及要求的最小子序列长度，研究人员经常会需要在其中找出GC-Ratio最高的子序列。

此题O(N^2)暴力求解即可, 这里因为是比较的是比例, 因此用
from fractions import Fraction
的Fraction类实现分数比较更加精确.
"""
from fractions import Fraction


class Solution(object):
    def max_gc_radio(self, s, n):
        if len(s) < n:
            return ""
        elif len(s) == n:
            return s
        highest_radio = Fraction(0, 1)
        highest_seq = s[0:n]
        for i in xrange(0, len(s) - n):
            for j in xrange(i + n, len(s) + 1):
                seq = s[i:j]
                seq_radio = Fraction(seq.count("G") + seq.count("C"), len(seq))
                if seq_radio > highest_radio:
                    highest_radio = seq_radio
                    highest_seq = seq
        return highest_seq


def main():
    print Solution().max_gc_radio(raw_input(), input())


if __name__ == '__main__':
    main()
