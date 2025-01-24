# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(idx):
            if idx >= n:
                return 0
            length = max(idx + 1, 1)
            cost = dfs(idx + length + 1)
            for i in range(idx + 1, min(idx + length + 1, n + 1)):
                cost = min(cost, dfs(i))
            return cost + prices[idx]
        return dfs(0)