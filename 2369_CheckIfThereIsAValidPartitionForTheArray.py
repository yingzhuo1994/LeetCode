# 1st solution
# O(n) time | O(n) space
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n + 1)]
        dp[-1] = True
        for i in reversed(range(n)):
            if i + 1 < n and nums[i] == nums[i + 1]:
                if dp[i + 2]:
                    dp[i] = dp[i + 2]
            if i + 2 < n and ((nums[i] == nums[i + 1] == nums[i + 2]) or (nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1)):
                if dp[i + 3]:
                    dp[i] = dp[i + 3]
        return dp[0]