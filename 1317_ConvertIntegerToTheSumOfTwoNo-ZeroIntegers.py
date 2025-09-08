# 1st solution
# O(n) time | O(1) space
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n // 2 + 1):
            if "0" in str(a):
                continue
            b = n - a
            if "0" in str(b):
                continue
            return [a, b]
        return [-1, -1]