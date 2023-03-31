# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return sum(nums[:n:2])
