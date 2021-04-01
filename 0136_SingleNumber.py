class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
                return nums[i]
                
