# 1st solution, dynamic programming
# O(kn) time | O(kn) space
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if len(prices) <= 1 or k == 0: 
            return 0

        profits = [prices[i+1] - prices[i] for i in range(n - 1)]
        if k > n//2: return sum(x for x in profits if x > 0)
        
        dp = [[0]*(k+1) for _ in range(n-1)] 
        mp = [[0]*(k+1) for _ in range(n-1)] 

        dp[0][1], mp[0][1] = profits[0], profits[0]

        for i in range(1, n-1):
            for j in range(1, k+1):
                dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + profits[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])

# 2nd solution, improved dynamic programming
# O(kn) time | O(kn) space
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) <= 1 or k == 0: 
            return 0

        delta = [prices[i+1]-prices[i] for i in range (len(prices)-1)]
        B = [sum(delta) for _, delta in groupby(delta, key=lambda x: x < 0)] 
        n = len(B)

        if k > n // 2: 
            return sum(x for x in B if x > 0)
        
        dp = [[0]*(k+1) for _ in range(n)] 
        mp = [[0]*(k+1) for _ in range(n)] 

        dp[0][1], mp[0][1] = B[0], B[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j] = max(mp[i-1][j-1], dp[i-1][j]) + B[i]
                mp[i][j] = max(dp[i][j], mp[i-1][j])

        return max(mp[-1])