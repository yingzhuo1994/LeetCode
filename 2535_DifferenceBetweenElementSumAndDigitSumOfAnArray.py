# 1st solution
# O(n) time | O(1) space
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = sum(nums)
        digitSum = sum(sum(map(int, list(str(num)))) for num in nums)
        return abs(elementSum - digitSum)
