# 1st solution
# O(nk) time | O(n + k) space
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n + k)]
        for i in range(n):
            value = 0
            for j in range(i - k, i):
                value = max(value, dp[j])
            dp[i] = value + nums[i]
        return max(dp[:-k])