# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        start = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ans = max(ans, i - start + 1)
            else:
                start = i
        start = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                ans = max(ans, i - start + 1)
            else:
                start = i
        return ans