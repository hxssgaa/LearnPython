# coding=utf-8
"""
寻找等差数列

题目标题：
在给定的区间范围内找出所有素数能构成的最大的等差数列（即等差数列包含的素数个数最多）。

这个题非常重要, 同时也非常难, 题目实际上就是要求一个有序序列中如何寻找最长的等差数列.

对于这个题, 可以用线性规划, 使得dp[i][j]相当于最后两个元素分别为nums[i]和nums[j]的最长等差数列.
那么很明显, 初始状况下, dp[0][i] = 2 (i=[1, n - 1]) 因为最后两个元素其中前一个为第一个的话, 那么很明显等差数列长度一定为2

那么这个题可以用two-pointers的方式, 遍历 i = [1, n - 1], 定义两个pointer j 和 k分别为i-1和i+1
再去寻找num[j]+num[k]==num[i]*2的j和k, 在遍历的时候根据num[j]+num[k] - num[i]*2的大小决定是j--还是k++,
那么我们可以得到当num[j]+num[k]==num[i]*2时候, dp[i][k] = dp[j][i] + 1
而当k移动的时候, 需要先设置dp[i][k] = 2, 因为这是个初始值

而对于序列的记录来说, 只要我们知道最后一个元素的下标, 以及公差, 就可以知道最后的结果.
"""
import math

from com.hxdavid.utils.utils import statistics


class Solution(object):
    def is_prime(self, n):
        if n <= 1:  # Don't forget to check if n is less or equal than 1.
            return False
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    @statistics()
    def get_max_array(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: list[int]
        """
        primes = filter(lambda x: self.is_prime(x), range(m, n + 1))
        if not primes:
            return []
        if len(primes) == 1:
            return [primes[0]]
        n, max_ap = len(primes), 2
        max_ap_start, max_ap_sub = 0, primes[1] - primes[0]

        # Suppose dp[i][j] is the length longest AP Whose last two elements are nums[i] and nums[j]
        dp = [[0] * n for _ in range(n)]
        for i in xrange(0, n - 1):
            dp[i][n - 1] = 2

        for i in xrange(n - 1, 0, -1):
            j = i - 1  # Choose j to the left of i
            k = i + 1  # Choose k to the right of j
            while j >= 0 and k <= n - 1:
                is_ap = (primes[j] + primes[k]) - 2 * primes[i]
                if is_ap < 0:  # Move k to the right to find larger result
                    k += 1
                elif is_ap > 0:  # Move j to the left to find smaller result
                    dp[j][i] = 2
                    j -= 1
                else:  # Result found, dp[i][k] = dp[j][i] + 1
                    dp[j][i] = dp[i][k] + 1
                    if dp[j][i] > max_ap or (dp[j][i] == max_ap and j < max_ap_start):
                        max_ap = dp[j][i]
                        max_ap_start = j
                        max_ap_sub = primes[k] - primes[i]
                    k += 1
                    j -= 1
            while j >= 0:  # Don't forget the last remaining two elements are still 2.
                dp[j][i] = 2
                j -= 1

        res = [primes[max_ap_start]] + [primes[i] for i in filter(
            lambda x: (primes[x] - primes[max_ap_start]) % max_ap_sub == 0, range(max_ap_start + 1, n))]

        # Get rid of non-AP numbers.
        for i in xrange(len(res)):
            if (res[i] - primes[max_ap_start]) // max_ap_sub != i:
                return res[:i]
        return res


def main():
    data = map(int, raw_input().split())
    print " ".join(map(str, Solution().get_max_array(data[0], data[1])))


if __name__ == '__main__':
    main()
