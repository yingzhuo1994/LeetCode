# 1st solution, dynamic programming
# O(kn) time | O(kn) space
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0: return 0
        n = len(prices)

        B = [prices[i+1] - prices[i] for i in range(len(prices) - 1)]
        if k > len(prices)//2: return sum(x for x in B if x > 0)
        
        dp = [[0]*(k+1) for _ in range(n-1)] 
        mp = [[0]*(k+1) for _ in range(n-1)] 

        dp[0][1], mp[0][1] = B[0], B[0]

        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + B[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])