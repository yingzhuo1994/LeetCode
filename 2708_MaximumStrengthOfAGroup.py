# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        mn = mx = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            mn, mx = min(mn, x, mn * x, mx * x), \
                     max(mx, x, mn * x, mx * x)
        return mx