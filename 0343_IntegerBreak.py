# 1st solution, Top-down
# O(n^2) time | O(n) space
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {1: 1}
        def dfs(target):
            if target in memo:
                return memo[target]
            ans = 1
            for num in range(1, target):
                ans = max(ans, num * (target - num), num * dfs(target - num))
            memo[target] = ans
            return ans
        return dfs(n)

# 2nd solution, Bottom-up
# O(n^2) time | O(n) space
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        for k in range(1, n + 1):
            for left in range(1, k):
                dp[k] = max(dp[k], left * (k - left), left * dp[k - left])
        return dp[n]

# 3rd solution, Math
# O(log(n)) time | O(1) space
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        count, res = divmod(n, 3)
        if res == 1:
            res += 3
            count -= 1
        elif res == 0:
            res = 1
        return pow(3, count) * res