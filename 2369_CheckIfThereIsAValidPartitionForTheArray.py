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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # Only record the most recent 3 indices
        dp = [True] + [False] * 2

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        for i in range(n):
            dp_index = i + 1
            ans = False
            if i > 0 and nums[i] == nums[i - 1]:
                ans |= dp[(dp_index - 2) % 3]
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                ans |= dp[(dp_index - 3) % 3]
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                ans |= dp[(dp_index - 3) % 3]
            dp[dp_index % 3] = ans

        return dp[n % 3]