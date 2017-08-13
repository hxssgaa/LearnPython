import math
from operator import add
from random import random

from pyspark import SparkContext


class Solution(object):
    def is_prime(self, n):
        if n <= 1:  # Don't forget to check if n is less or equal than 1.
            return False
        for i in xrange(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def get_max_array(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: list[int]
        """
        primes = filter(lambda x: self.is_prime(x), range(m, n))
        if not primes:
            return []
        if len(primes) == 1:
            return [primes[0]]
        n, max_ap = len(primes), 2
        max_ap_end, max_ap_sub = 1, primes[1] - primes[0]

        # Suppose dp[i][j] is the length longest AP Whose last two elements are nums[i] and nums[j]
        dp = [[0] * n for _ in range(n)]
        for i in xrange(1, n):
            dp[0][i] = 2

        for i in xrange(1, n):
            j = i - 1  # Choose i to the left of j
            k = i + 1  # Choose k to the right of j
            while j >= 0 and k <= n - 1:
                is_ap = (primes[j] + primes[k]) - 2 * primes[i]
                if is_ap < 0:  # Move k to the right to find larger result
                    dp[i][k] = 2
                    k += 1
                elif is_ap > 0:  # Move j to the left to find smaller result
                    j -= 1
                else:  # Result found, dp[i][k] = dp[j][i] + 1
                    dp[i][k] = dp[j][i] + 1
                    if dp[i][k] > max_ap:
                        max_ap = dp[i][k]
                        max_ap_end = k
                        max_ap_sub = primes[k] - primes[i]
                    k += 1
                    j -= 1
            while k <= n - 1:  # Don't forget the last remaining two elements are still 2.
                dp[i][k] = 2
                k += 1

        res = [primes[i] for i in filter(lambda x: (primes[max_ap_end] - primes[x]) % max_ap_sub == 0,
                                         range(0, max_ap_end))] + [primes[max_ap_end]]
        for i in xrange(len(res)):
            if (primes[max_ap_end] - res[i]) // max_ap_sub != len(res) - i:
                return res[i:]
        return res


if __name__ == '__main__':
    sc = SparkContext("local[8]", "Simple App")
    partitions = 10
    n = 100000


    def f(i):
        return Solution().get_max_array(i, i + 1000)


    res_arr = sc.parallelize(range(0, n + 1, 1000), partitions).map(f).reduce(add)
    print("result array is %s" % " ".join(map(str, res_arr)))
