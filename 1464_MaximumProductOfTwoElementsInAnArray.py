# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = -1
        for num in nums:
            if num > first:
                first, second = num, first
            elif num > second:
                second = num
        return (first - 1) * (second - 1)