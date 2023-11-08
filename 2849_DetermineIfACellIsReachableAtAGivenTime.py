# 1st solution
# O(1) time | O(1) space
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(fx - sx), abs(fy - sy))
        if dist > t:
            return False
        if dist == 0:
            return t == 0 or t > 1
        return True