# 1st solution
# O(n) time | O(1) space
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        minErrorNum = float("inf")
        maxErrorNum = float("-inf")
        for i, num in enumerate(nums):
            if self.isOutOfOrder(nums, i):
                minErrorNum = min(minErrorNum, num)
                maxErrorNum = max(maxErrorNum, num)

        if minErrorNum == float("inf"):
            return 0
        
        minIndex = 0
        while nums[minIndex] <= minErrorNum:
            minIndex += 1
        
        maxIndex = len(nums) - 1
        while nums[maxIndex] >= maxErrorNum:
            maxIndex -= 1
        return maxIndex - minIndex + 1

    def isOutOfOrder(self, nums, idx):
        if idx == 0:
            return nums[idx] > nums[idx + 1]
        elif idx == len(nums) - 1:
            return nums[idx] < nums[idx - 1]
        else:
            return nums[idx - 1] > nums[idx] or nums[idx] > nums[idx + 1]