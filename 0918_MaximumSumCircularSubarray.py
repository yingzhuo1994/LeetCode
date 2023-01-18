# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total, curMax, curMin = 0, 0, 0
        maxSum = minSum = nums[0]
        for num in nums:
            curMax = max(curMax + num, num)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + num, num)
            minSum = min(minSum, curMin)
            total += num
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum