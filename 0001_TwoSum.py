class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        >>> nums = [2,7,11,15], target = 9
        >>> twoSum(nums, target)
        [0,1]
        >>> nums = [3,2,4], target = 6
        >>> twoSum(nums, target)
        [1,2]
        >>> nums = [3,3], target = 6
        >>> twoSum(nums, target)
        [0,1]
        """
        if len(nums) < 2:
            return 'the length of nums must be larger than 2'
        else:
            i = 0
            while i < len(nums) - 1:
                j = i + 1
                while j < len(nums):
                    if nums[i] + nums[j] == target:
                        return [i, j]
                    j += 1
                i += 1
            return 'no solution exists!'
