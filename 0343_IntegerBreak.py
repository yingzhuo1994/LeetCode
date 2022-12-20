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