# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        
        diff = [prices[i+1] - prices[i] for i in range(n-1)]
        dp, dp_max = [0]*(n + 1), [0]*(n + 1)
        for i in range(n-1):
            dp[i] = diff[i] + max(dp_max[i-3], dp[i-1])
            dp_max[i] = max(dp_max[i-1], dp[i])
            
        return dp_max[-3]

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        dp = [0 for _ in range(n + 2)]
        
        for i in range(1, n):
            dp[i] = dp[i-1]
            for j in range(i):
                profit = prices[i] - prices[j]
                dp[i] = max(dp[i], profit + dp[j - 2])

        return max(dp)
                