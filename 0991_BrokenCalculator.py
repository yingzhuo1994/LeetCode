# 1st solution
# O(log(target)) time | O(1) space
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            count += 1
            if target & 1: 
                target += 1
            else: 
                target //= 2

        return count + startValue - target
        