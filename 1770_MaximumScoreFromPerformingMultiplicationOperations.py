# 1st solution, TLE
# O(n^2) time | O(n^2) space
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(nums)
        n = len(multipliers)
        memo = {}
        k = n - 1
        for left in range(k + 1):
            right = left + m - 1 - k
            memo[(left, right)] = max(multipliers[k] * nums[left], multipliers[k] * nums[right])
        for k in reversed(range(n - 1)):
            for left in range(k + 1):
                right = left + m - 1 - k
                memo[(left, right)] = max(multipliers[k] * nums[left] + memo[(left + 1, right)], multipliers[k] * nums[right] + memo[(left, right - 1)])
        
        return memo[(0, m - 1)]