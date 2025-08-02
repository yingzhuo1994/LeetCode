# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in reversed(range(n)):
            ans = max(ans, abs(nums[i] - nums[i-1]))
        return ans