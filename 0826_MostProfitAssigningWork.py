# 1st solution
# O(n * log(n) + m * log(n)) time | O(n) space
# where n = len(profit) and m = len(worker)
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

# 2nd solution
# O(n * log(n) + m * log(m)) time | O(n) space
# where n = len(profit) and m = len(worker)
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = j = max_profit = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            ans += max_profit
        return ans