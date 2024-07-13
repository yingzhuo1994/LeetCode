# 1st solution
# O(n) time | O(1) space
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        start = 0
        for i, num in enumerate(nums):
            if bin(num).count("1") != bin(nums[start]).cont(1):
                nums[start:i] = sorted(nums[start:i])
                start = i
        if start != len(nums) - 1:
            nums[start:] = sorted(nums[start:])
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        return True