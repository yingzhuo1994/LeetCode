# 1st solution
# O(n) time | O(n) space
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m = max(nums)
        if m <= 0:
            return m
        ans = sum(num for num in set(nums) if num > 0)
        return ans