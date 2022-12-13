# 1st solution, top-down dp
# O(n^3) time | O(n^2) space
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        memo = {}
        def helper(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left >= right:
                memo[(left, right)] = 0
                return 0
            ans = float("inf")
            for i in range(left, right):
                leftVal = helper(left, i - 1)
                rightVal = helper(i + 1, right)
                ans = min(ans, max(leftVal, rightVal) + i)
            memo[(left, right)] = ans
            return ans
        return helper(1, n)

# 2nd solution, bottom-up dp
# O(n^3) time | O(n^2) space
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for lo in range(n, 0, -1):
            for hi in range(lo+1, n+1):
                dp[lo][hi] = float("inf")
                for x in range(lo, hi):
                    dp[lo][hi] = min(dp[lo][hi], x + max(dp[lo][x-1], dp[x+1][hi]))
        return dp[1][n]