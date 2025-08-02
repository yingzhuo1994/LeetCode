# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        n = len(energyDrinkA)
        dp = [[0, 0] for _ in range(n + 2)]
        for i in range(n):
            dp[i][0] = max(dp[i-1][0], dp[i-2][1]) + energyDrinkA[i]
            dp[i][1] = max(dp[i-1][1], dp[i-2][0]) + energyDrinkB[i]
        return max(dp[n - 1])