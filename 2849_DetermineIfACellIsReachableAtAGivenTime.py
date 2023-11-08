# 1st solution
# O(1) time | O(1) space
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dist = max(abs(fx - sx), abs(fy - sy))
        if dist != 0:
            return dist <= t
        else:
            return t != 1