class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1st two-pass solution
        # O(2n) time | O(1) space
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
        
        # 2nd one-pass solution
        # O(n) time | O(1) space
        """ Since all numbers befor zero index have been checked, we could move forward directly.
            But for numbers after two index, after we change the numbers, we need to check current number again.
        """ 
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
            elif nums[i] == 1:
                i += 1
            
        
