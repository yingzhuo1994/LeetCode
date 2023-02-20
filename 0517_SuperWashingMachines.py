# 1st solution
# O(n) time | O(1) space
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n != 0:
            return -1
        target, res, toRight = total // n, 0, 0
        for m in machines:
            toRight = m + toRight - target
            res = max(res, abs(toRight), m - target)
        return res