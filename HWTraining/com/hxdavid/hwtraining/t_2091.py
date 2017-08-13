# coding=utf-8
"""
称砝码

现有一组砝码，重量互不相等，分别为m1、m2……mn；他们可取的最大数量分别为x1、x2……xn。现在要用这些砝码去称物体的重量，问能称出多少中不同的重量。

注：
称重重量包括0
要对输入数据进行校验

方法原型：public static int fama(int n, int[] weight, int[] nums)

这个题可以用dp求解, dp[i]表示重量为i的砝码是否被称出
但是用dp求解需要首先知道所有砝码最大的重量, 然后利用
如果 dp[z-weight[i]] == True:
那么 dp[i] = True的方式进行dp的计算, 最后计算dp为真的个数即可, 这样的话要求最大重量不能太高

或者直接利用第二种方法, 通过set的方式计算所有可能出现的重量个数即可.
第二种用set计算的办法效率优于dp的第一种
"""


class Solution(object):
    def fama(self, n, weight, nums):
        dp = [False] * 1000
        dp[0] = True
        sum_w = sum(weight[i] * nums[i] for i in range(n))
        for i in range(0, n):  # total count of fama
            for j in range(0, nums[i]):  # each num of fama.
                for z in range(sum_w, weight[i] - 1, -1):
                    if dp[z - weight[i]]:
                        dp[z] = True
        return sum(dp)

    def fama2(self, n, weight, nums):
        """
        Second method outperforms the first one, about 2x times faster than previous one.
        """
        ws = {0}
        for i in range(0, n):
            ts = set()
            for j in range(0, nums[i]):
                for w in ws:
                    ts.add(weight[i] * (j + 1) + w)
            ws = ws.union(ts)
            for j in range(0, nums[i]):
                ws.add(weight[i] * (j + 1))
        return len(ws)


def main():
    n = input()
    weight = []
    nums = []
    for _ in range(n):
        weight.append(input())
    for _ in range(n):
        nums.append(input())
    print Solution().fama(n, weight, nums)


if __name__ == '__main__':
    main()
