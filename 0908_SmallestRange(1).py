# 1st solution
# O(n) time | O(1) space
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxVal = max(nums)
        minVal = min(nums)
        return max(maxVal - minVal - 2 * k, 0)