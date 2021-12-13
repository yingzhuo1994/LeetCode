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