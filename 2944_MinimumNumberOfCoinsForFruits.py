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

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return prices[0]
        dp = [float("inf")] * (n + 1)
        dp[-1] = 0
        dp[n - 1] = prices[-1]
        minHeap = [[prices[n - 1], n - 1]]
        for i in reversed(range(n - 1)):
            while minHeap and minHeap[0][1] > i + (i + 1):
                heappop(minHeap)
            cost = prices[i] + min(minHeap[0][0], dp[min(i + i + 2, n)])
            dp[i] = cost
            heappush(minHeap, [cost, i])
        return dp[0]