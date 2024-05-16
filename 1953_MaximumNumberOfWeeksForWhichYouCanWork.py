# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)
        maxVal = max(milestones)
        preSum = total - maxVal
        if preSum < maxVal:
            return preSum * 2 + 1
        else:
            return total