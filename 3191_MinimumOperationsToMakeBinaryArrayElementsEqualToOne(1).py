# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ans += 1
        if nums[n - 2] and nums[n - 1]:
            return ans
        else:
            return -1