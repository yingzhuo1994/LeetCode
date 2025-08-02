# 1st solution
# O(n) time | O(1) space
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        pivotal = -1
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                continue
            else:
                pivotal = i + 1
                break
        if pivotal < 0:
            return True
        for i in range(pivotal, n - 1):
            if nums[i] > nums[i + 1]:
                return False
        return nums[0] >= nums[-1]