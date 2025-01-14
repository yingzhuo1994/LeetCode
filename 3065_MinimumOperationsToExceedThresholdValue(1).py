# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(x < k for x in nums)