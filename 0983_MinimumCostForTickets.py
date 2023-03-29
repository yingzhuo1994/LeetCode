# 1st solution
# O(3^n) time | O(n) space
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dfs(idx, date):
            start = idx
            while start < len(days) and days[start] < date:
                start += 1
            if start >= len(days):
                return 0
            total = float("inf")

            for day, cost in zip([1, 7, 30], costs):
                cur_cost = cost + dfs(start, days[start] + day)
                total = min(total, cur_cost)
            return total

        return dfs(0, -1)


# 2nd solution
# O(n) time | O(n) space
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1] + 1)]
        travelSet = set(days)
        for i in range(days[-1] + 1):
            if i not in travelSet:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 30)] + costs[2])
        return dp[-1]