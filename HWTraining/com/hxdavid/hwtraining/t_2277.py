# coding=utf-8
"""
购物单

王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
    设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
    请你帮助王强设计一个满足要求的购物单。


算法思路:
这个题为典型的0-1背包问题:
我们有n种物品，物品j的重量为wj，价格为pj。
我们假定所有物品的重量和价格都是非负的。背包所能承受的最大重量为W。
如果限定每种物品只能选择0个或1个，则问题称为0-1背包问题

3000 10
800 2 0
500 5 5
400 5 1
700 3 0
300 2 2
400 5 1
700 4 0
300 2 0
1000 2 0
300 7 0

1000 6
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
200 5 4

设dp(i,j)为前i件物品, 剩余背包容量为j所能取得的最大价值.
那么其实就变成了是不是要选第j件物品的问题, 要么选, 要么不选, 取最大值即可.
总的来说dp(i,j) = max(dp(i-1,j), v[i] + dp(i-1,j-w[i]))
其中v[i]表示第i件物品的价值, w[i]表示第i件物品的重量.

这道题可以用变种的0-1背包问题解决
相当于只需要考虑主件物品, 存放主件和附件的依赖关系, 那么购买主件则有5种情况:
1. 不购买主件            dp(i,j) = dp(i-1,j)
2. 只购买主件            dp(i,j) = v[i] + dp(i-1,j-w[i])
3. 购买主件和附件1       dp(i,j) = v[i] + v[i1] + dp(i-1,j-w[i]-w[i1])
4. 购买主件和附件2       dp(i,j) = v[i] + v[i2] + dp(i-1,j-w[i]-w[i2])
5. 购买主件和附件1,附件2  dp(i,j) = v[i] + v[i1] + v[i2] + dp(i-1,j-w[i]-w[i2]-w[i2])
"""
from collections import defaultdict


class Solution(object):
    def max_sum(self, n, w, weight, value, belong):
        """
        :type n: int
        :type w: int
        :type weight: list[int]
        :type value: list[int]
        :type belong: list[int]
        :rtype: int
        """
        dp = [0] * (w + 1)
        acc_map = defaultdict(list)
        for i, e in enumerate(belong):
            if e:
                acc_map[e].append(i)
        for i in range(1, n + 1):
            if belong[i]:
                continue
            if i not in acc_map or len(acc_map[i]) == 0:
                for j in range(w, weight[i] - 1, -1):  # for j < w[i]: dp[j] = 0
                    dp[j] = max(dp[j],  # don't buy main part i
                                dp[j - weight[i]] + value[i],  # only buy main part i
                                )
            if i in acc_map and len(acc_map[i]) >= 1:
                for j in range(w, weight[i] + weight[acc_map[i][0]] - 1, -1):
                    # buy main part and accessory 1 part
                    dp[j] = max(dp[j], dp[j - weight[i] - weight[acc_map[i][0]]] + value[i] + value[acc_map[i][0]])
            if i in acc_map and len(acc_map[i]) == 2:
                for j in range(w, weight[i] + weight[acc_map[i][1]] - 1, -1):
                    # buy main part and accessory 2 part
                    dp[j] = max(dp[j], dp[j - weight[i] - weight[acc_map[i][1]]] + value[i] + value[acc_map[i][1]])
                for j in range(w, weight[i] + weight[acc_map[i][0]] + weight[acc_map[i][1]] - 1, -1):
                    # buy main part and accessory 1 and 2 part
                    dp[j] = max(dp[j], dp[j - weight[i] - weight[acc_map[i][0]] - weight[acc_map[i][1]]] +
                                          value[i] + value[acc_map[i][0]] + value[acc_map[i][1]])
        return dp[w]


def main():
    n, m = (int(e) for e in raw_input().split())
    weight, value, belong = [0], [0], [0]
    for i in range(m):
        v, p, q = (int(e) for e in raw_input().split())
        weight.append(v / 10)
        value.append(p * v / 10)
        belong.append(q)
    print Solution().max_sum(m, n / 10, weight, value, belong) * 10


if __name__ == '__main__':
    main()
