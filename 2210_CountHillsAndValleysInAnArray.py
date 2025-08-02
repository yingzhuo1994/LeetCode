# 1st solution
# O(n) time | O(1) space 
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        i = 1
        left = 0
        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[left] == nums[i]:
                left += 1
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j < len(nums):
                if nums[i] > nums[left] and nums[i] > nums[j]:
                    ans += 1
                elif nums[i] < nums[left] and nums[i] < nums[j]:
                    ans += 1
            left = i
            i = j
        return ans