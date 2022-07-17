# 1st solution, TLE
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

# 2nd solution
# O(nk) time | O(nk) space
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
        MOD = 10**9 + 7
        for j in range(1, n + 1):
            dp[0][j] = 1
        
        for j in range(2, n + 1):
            for i in range(1, k + 1):
                if i - j >= 0:
                    last = dp[i - j][j - 1]
                else:
                    last = 0
                dp[i][j] = dp[i-1][j] - last + dp[i][j - 1]
                dp[i][j] %= MOD

        return dp[-1][-1]