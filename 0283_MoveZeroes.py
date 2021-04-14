class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPointer = len(nums)
        for i in range(len(nums)):
            if nums[i] == 0 and zeroPointer == len(nums):
                zeroPointer = i
            else:
                if nums[i] != 0 and i > zeroPointer:
                    nums[i], nums[zeroPointer] = nums[zeroPointer], nums[i]
                    zeroPointer += 1
        return nums
