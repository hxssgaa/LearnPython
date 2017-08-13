# coding=utf-8
"""
火车进站

给定一个正整数N代表火车数量，0<N<10，接下来输入火车入站的序列，一共N辆火车，
每辆火车以数字1-9编号。要求以字典序排序输出火车出站的序列号。

这个题目非常重要, 其实相当于就是求一个栈所有可能的出栈序列.
这个题首先需要一个初始的序列,以及栈序列, 注意的是初试序列刚开始需要reverse一下, 因为
出栈序列才是输出序列.

那么可以分成几种情况:
- 如果初始序列,和栈都为空,那么就添加输出序列到结果数组中.
- 如果栈和初始序列都不为空,那么分成出栈和入栈两种情况考虑
- 如果只有栈不为空,那么只能出栈
- 如果初始序列不为空,则将初始序列入栈.

注意的是递归的写法,一般对于双重数组,或者遍历而言,利用cur和res,return void的
方法更加方便, 一定要掌握这种递归的遍历写法.

此题还需要注意初始序列一定要reverse, 这样才能形成正确的栈. 注意栈stk才是重点, nums只是个辅助输入变量
"""


class Solution(object):
    def pop_seq_helper(self, nums, stk, cur, res):
        """
        :type nums: list[str]
        :type stk: list[str]
        :type cur: list[str]
        :type res: list[list[str]]
        """
        if not nums and not stk:
            res.append(cur[:])
            return res
        if stk and nums:  # stack and sequence both not empty, push sequence or pop.
            # pop sequence, and append it to the result.
            self.pop_seq_helper(nums, stk[:len(stk) - 1], cur + [stk[-1]], res)
            # push sequence.
            self.pop_seq_helper(nums[:len(nums) - 1], stk + [nums[-1]], cur, res)
        elif stk and not nums:
            # pop sequence
            self.pop_seq_helper(nums, stk[:len(stk) - 1], cur + [stk[-1]], res)
        elif not stk and nums:
            # push sequence.
            self.pop_seq_helper(nums[:len(nums) - 1], stk + [nums[-1]], cur, res)

    def pop_seq(self, nums):
        """
        :type nums: list[str]
        :rtype: list[list[str]]
        """
        res = []
        self.pop_seq_helper(list(reversed(nums)), [], [], res)
        return res


def main():
    n = input()
    l = raw_input()
    print "\n".join(sorted([" ".join(e) for e in Solution().pop_seq(l.split())]))


if __name__ == '__main__':
    main()
