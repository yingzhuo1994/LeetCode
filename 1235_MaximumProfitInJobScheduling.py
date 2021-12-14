# 1st solution, TLE
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(profit)
        table = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        table.sort(key = lambda v: v[1])

        dp = [table[i][2] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if table[j][1] <= table[i][0] and dp[j] + table[i][2] > dp[i]:
                    dp[i] = dp[j] + table[i][2]
        return max(dp)

# 2nd solution
# O(n*log(n)) time | O(n) space
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dpEndTime = [0]
        dpProfit = [0]
        for start, end, profit in jobs:
            i = bisect.bisect_right(dpEndTime, start) - 1
            if dpProfit[i] + profit > dpProfit[-1]:
                dpEndTime.append(end)
                dpProfit.append(dpProfit[i] + profit)
        return dpProfit[-1]