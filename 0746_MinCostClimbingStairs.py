# 1st solution
# O(n) time | O(n) space
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2:
            return min(cost)
        cost.append(0)
        dp = [float("inf") for _ in range(n + 1)]

        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = min(dp[i-2:i]) + cost[i]
        
        return dp[-1]