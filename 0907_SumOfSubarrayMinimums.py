# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        ans = sum(arr)
        level = arr
        for L in range(1, n):
            newLevel = []
            for i in range(n - L):
                value = min(level[i], arr[i+L])
                ans += value
                newLevel.append(value)
            ans %= MOD
            level = newLevel
        return ans