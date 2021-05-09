class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        
        two = len(nums) - 1
        for i in reversed(range(len(nums))):
            if nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
        
