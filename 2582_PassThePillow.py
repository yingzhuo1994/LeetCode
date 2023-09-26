# 1st solution
# O(1) time | O(1) space
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        k, r = divmod(time, n - 1)
        if k & 1:
            return n - r
        else:
            return r + 1