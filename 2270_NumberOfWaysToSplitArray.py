# 1st solution
# O(n) time | O(1) space
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        ans = 0
        for i in range(len(nums) - 1):
            prefix += nums[i]
            if prefix >= total - prefix:
                ans += 1
        return ans