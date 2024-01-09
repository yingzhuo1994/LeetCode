class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        preSum = 0
        for i in range(len(nums)):
            if preSum == total - preSum - nums[i]:
                return i
            preSum += nums[i]
        return -1