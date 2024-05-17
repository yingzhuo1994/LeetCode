# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tasks = [[d, p] for d, p in zip(difficulty, profit)]
        tasks.sort()
        dp = {}
        maxProfit = 0
        for d, p in tasks:
            maxProfit = max(maxProfit, p)
            dp[d] = max(dp.get(d, 0), maxProfit)
        keys = sorted(list(dp.keys()))
        ans = 0
        for d in worker:
            idx = bisect.bisect_right(keys, d) - 1
            if idx >= 0:
                ans += dp[keys[idx]]
        return ans
