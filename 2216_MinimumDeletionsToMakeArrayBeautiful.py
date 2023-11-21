# 1st solution
# O(n) time | O(1) space
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        i = 0
        k  = 1
        ans = 0
        while i < len(nums):
            if i + k < len(nums):
                if nums[i] == nums[i + k]:
                    ans += 1
                    k += 1
                else:
                    i = i + k + 1
                    k = 1
            else:
                ans += 1
                i = i + k + 1
        return ans