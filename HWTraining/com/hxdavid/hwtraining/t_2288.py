# coding=utf-8
"""
合唱队

计算最少出列多少位同学，使得剩下的同学排成合唱队形
说明：
N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1，2…，K，他们的身高分别为T1，T2，…，TK，

则他们的身高满足存在i（1<=i<=K）使得Ti<T2<......<Ti-1<Ti>Ti+1>......>TK。

你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。
"""


# 40 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
# lis[i] 为T1...Ti的最长递增子序列, lds[i] 为Ti...TN-1最长递减子序列
# 注意, 只有LCS与LDS这样的DP问题, 是不需要用DP[N+1]的, 否则的话, 两者坐标不对应.
# LCS与LDS算法复杂度为O(N^2), 其实就是用i = 2....N, j == 1....i 这样的方法计算DP[i]即可.
# 在华为OJ中,一旦有n可以先用input(),再用raw_input().split()来获取数据,切记不可以直接raw_input()中取数据
class Solution(object):
    def min_stu(self):
        n = input()
        nums = raw_input().split()
        hs = [int(e) for e in nums]
        lis, lds = [1] * n, [1] * n
        for i in xrange(1, n):
            for j in xrange(0, i):
                if hs[j] < hs[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1
        for i in xrange(n - 2, -1, -1):
            for j in xrange(n - 1, i, -1):
                if hs[j] < hs[i] and lds[j] + 1 > lds[i]:
                    lds[i] = lds[j] + 1
        return n - max(lis[i] + lds[i] for i in range(0, n)) + 1


if __name__ == '__main__':
    print Solution().min_stu()
