# O(n) time | O(1) space
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        total = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                total += nums[i]
            else:
                total = nums[i]
            ans = max(ans, total)
        return ans