# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(pos, neg)