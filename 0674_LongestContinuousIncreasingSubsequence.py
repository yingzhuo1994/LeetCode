# 1st solution
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        start  = 0 
        for i in range(1, len(nums)):
            num = nums[i]
            if num > nums[i - 1]:
                ans = max(ans, i - start + 1)
            else:
                start = i
        return ans