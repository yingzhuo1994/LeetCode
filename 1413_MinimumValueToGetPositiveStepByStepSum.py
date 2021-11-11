# 1st solution
# O(n) time | O(1) space
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        curSum = 1
        for num in nums:
            curSum += num
            if curSum < 1:
                startValue += 1 - curSum
                curSum = 1
        return startValue