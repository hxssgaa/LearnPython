# coding=utf-8
"""
201301 JAVA题目0-1级

编写一个函数，传入一个int型数组，返回该数组能否分成两组，使得两组中各元素加起来的和相等，
并且，所有5的倍数必须在其中一个组中，所有3的倍数在另一个组中（不包括5的倍数），能满足以上条件，返回true；不满足时返回false。

题目思路:
这个题考察DFS

实际上, 对于5的倍数和3的倍数, 我们可以先计算5的倍数以及3的倍数的分别的和, 那么再计算剩下的元素的和和剩下的元素
那么就是寻找剩下元素的某个子集X使得
sum(X) + sum5 = sum(other) - sum(X) + sum3

于是我们即可从other中的元素作DFS求解其和是否等于 (sum(other) + sum3 - sum5) / 2即可.
注意这里的DFS需要从-1开始, temp为0, 否则会出问题, 一般的temp都要以0开始, 这个需要非常注意, 可以利用-1的下标省去一层循环

"""


class Solution(object):
    def is_split_half_sum_equal_helper(self, data, s, temp, target):
        if temp == target:
            return True
        if s >= len(data) - 1:
            return False

        for i in xrange(s + 1, len(data)):
            if self.is_split_half_sum_equal_helper(data, i, temp + data[i], target):
                return True

        return False

    def is_split_half_sum_equal(self, data):
        if not data or sum(data) % 2 != 0:
            return False
        sum5, sum3, sum_other, arr_other = 0, 0, 0, []
        for e in data:
            if e % 5 == 0:
                sum5 += e
            elif e % 3 == 0:
                sum3 += e
            else:
                sum_other += e
                arr_other.append(e)
        return self.is_split_half_sum_equal_helper(arr_other, -1, 0, (sum_other + sum3 - sum5) // 2)


def main():
    data = []
    for _ in xrange(input()):
        data.append(input())
    print "true" if Solution().is_split_half_sum_equal(data) else "false"


if __name__ == '__main__':
    main()
