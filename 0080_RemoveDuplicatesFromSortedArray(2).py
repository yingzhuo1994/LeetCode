from tracemalloc import start


# 1st solution
# O(n) time | O(1) space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        startIdx = 0
        currentNum = None
        count = 0
        for num in nums:
            if currentNum != num:
                currentNum = num
                count = 1
            else:
                count += 1
            if count <= 2:
                nums[startIdx] = num
                startIdx += 1
        return nums
