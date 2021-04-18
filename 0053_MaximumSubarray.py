class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # O(n) time | O(1) space
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                nums[i + 1] += nums[i]
        return max(nums)
