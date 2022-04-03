# 1st solution
# O(n) time | O(1) space
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstDecreseIndex = len(nums) - 1
        while firstDecreseIndex > 0:
            if nums[firstDecreseIndex] <= nums[firstDecreseIndex - 1]:
                firstDecreseIndex -= 1
            else:
                break
        if firstDecreseIndex == len(nums) - 1:
            self.swap(nums, firstDecreseIndex, firstDecreseIndex - 1)
        elif firstDecreseIndex == 0:
            self.reverseNums(nums, firstDecreseIndex, len(nums) - 1)
        else:
            frontIndex = firstDecreseIndex - 1
            value = nums[frontIndex]
            self.reverseNums(nums, firstDecreseIndex, len(nums) - 1)
            nextLargerIndex = self.searchLargerValue(nums, value, firstDecreseIndex, len(nums) - 1)
            self.swap(nums, frontIndex, nextLargerIndex)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
    
    def reverseNums(self, nums, start, end):
        while start < end:
            self.swap(nums, start, end)
            start += 1
            end -= 1
    
    def searchLargerValue(self, nums, value, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= value:
                left = mid + 1
            else:
                right = mid
        return left

        