# 1st solution, TLE
from math import factorial
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        def countInverserPairs(left_n, left_k):
            if left_k == 0:
                memo[(left_n, left_k)] = 1
                return 
            if left_n <= 1:
                memo[(left_n, left_k)] = 0
                return
            count = 0
            for i in range(left_n):
                target_k = left_k - i
                if target_k < 0:
                    break
                if (left_n - 1, target_k) not in memo:
                    countInverserPairs(left_n - 1, target_k)
                count += memo[(left_n - 1, target_k)]
            count %= MOD
            memo[(left_n, left_k)] = count


        MOD = 10**9 + 7

        memo = {}
        countInverserPairs(n, k)
        return memo[(n, k)]
