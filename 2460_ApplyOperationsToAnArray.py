# 1st solution
# O(n) time | O(1) space
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] += nums[i + 1]
                nums[i + 1] = 0
        
        j = 0
        for i in range(n):
            if nums[i] == 0:
                j = max(i, j)
                while j < n and nums[j] == 0:
                    j += 1
                if j < n and nums[j] > 0:
                    nums[i] = nums[j]
                    nums[j] = 0
                    j += 1
            if j == n:
                break
        return nums