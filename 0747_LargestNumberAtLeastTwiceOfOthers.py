# 1st solution
# O(n) time | O(1) space
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = nums[0]
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                idx = i
        
        for i in range(len(nums)):
            if i == idx:
                continue
            if nums[i] * 2 > largest:
                return -1
        return idx