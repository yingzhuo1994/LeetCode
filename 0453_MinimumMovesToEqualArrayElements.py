# 1st solution
# O(n) time | O(1) space
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        a = min(nums)
        return s - a * n