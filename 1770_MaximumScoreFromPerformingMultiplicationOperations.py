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
            memo[(k, left)] = max(multipliers[k] * nums[left], multipliers[k] * nums[right])
        for k in reversed(range(n - 1)):
            for left in range(k + 1):
                right = left + m - 1 - k
                memo[(k, left)] = max(multipliers[k] * nums[left] + memo[(k + 1, left + 1)], multipliers[k] * nums[right] + memo[(k + 1, left)])
        
        return memo[(0, 0)]

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(nums)
        n = len(multipliers)

        dp = [[0 for _ in range(k + 1)] for k in range(n + 1)]
        for k in reversed(range(n)):
            for left in range(k + 1):
                right = left + m - 1 - k
                dp[k][left] = max(multipliers[k] * nums[left] + dp[k + 1][left + 1], multipliers[k] * nums[right] + dp[k + 1][left])
        
        return dp[0][0]