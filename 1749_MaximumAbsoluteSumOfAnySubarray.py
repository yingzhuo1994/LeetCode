# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = abs(nums[0])
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            if curSum < 0:
                curSum = 0
                start = i + 1
            else:
                ans = max(ans, curSum)
        curSum = 0
        for i, num in enumerate(nums):
            curSum += num
            if curSum > 0:
                curSum = 0
            else:
                ans = max(ans, -curSum)
        return ans