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
            for i in range(idx + 1, n):
                profit = prices[i] - prices[idx] - fee
                new = max([dfs(j) for j in range(i + 1, n)] + [0])
                ans = max(ans, profit + new)
            memo[idx] = ans
            return ans
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        print(sorted(list(memo.items())))
        return ans