# 1st solution, TLE
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(idx, left, targetProfit):
            if left == 0 or idx == len(group):
                if targetProfit <= 0:
                    return 1
                return 0

            if group[idx] > left:
                return dfs(idx+1, left, targetProfit)
            count = dfs(idx + 1, left - group[idx], targetProfit - profit[idx]) % MOD
            count += dfs(idx + 1, left, targetProfit) % MOD
            return count
        return dfs(0, n, minProfit)