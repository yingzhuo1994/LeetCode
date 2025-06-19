# 1st solution
# O(n) time | O(n) space
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, j = 1, 0
        for i in range(len(nums)):
            if nums[i] - nums[j] > k:
                res += 1
                j = i
        return res