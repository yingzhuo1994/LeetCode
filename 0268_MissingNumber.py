# Gauss' Formula
# O(n) time | O(1) space
# sum() function costs O(n) time
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (1 + n) * n // 2 - sum(nums)
