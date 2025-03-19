# 1st solution
# O(n) time | O(n) space
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left = nums[:]
        right = nums[:]
        for i in range(1, n):
            left[i] = max(left[i], left[i-1])
        for i in reversed(range(n - 1)):
            right[i] = min(right[i], right[i+1])
        for i in range(n - 1):
            if left[i] <= right[i + 1]:
                return i + 1