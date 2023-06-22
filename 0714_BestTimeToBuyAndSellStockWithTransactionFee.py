# 1st solution, TLE
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            if idx >= n:
                return 0
            ans = 0
            new = max([dfs(i) for i in range(idx + 1, n)] + [prices[i] - prices[idx] - fee + dfs(i) for i in range(idx + 1, n)] + [0])
            ans = max(ans, new)
            memo[idx] = ans
            return ans
        
        ans = dfs(0)
        print(sorted(list(memo.items())))
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy = [0] * n
        sell = [0] * n
        buy[0]= -prices[0]

        for i in range(1, n):
            # keep the same as day i-1, or buy from sell status at day i-1
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
            # keep the same as day i-1, or sell from buy status at day i-1
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i] - fee)
        
        return sell[n - 1]

# 3rd solution
# O(n) time | O(1) space
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy = [0, 0]
        sell = [0, 0]
        buy[0]= -prices[0]

        for i in range(1, n):
            # keep the same as day i-1, or buy from sell status at day i-1
            buy[1] = max(buy[0], sell[0] - prices[i])
            # keep the same as day i-1, or sell from buy status at day i-1
            sell[1] = max(sell[0], buy[0] + prices[i] - fee)
            
            buy[0] = buy[1]
            sell[0] = sell[1]
        
        return sell[1]