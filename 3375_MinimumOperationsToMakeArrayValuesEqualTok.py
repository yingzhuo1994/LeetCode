# 1st solution
# O(n) time | O(n) space
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        if minVal < k:
            return -1
        vals = set(nums)
        if minVal == k:
            return len(vals) - 1
        return len(vals)