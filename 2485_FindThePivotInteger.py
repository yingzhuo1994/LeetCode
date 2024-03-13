# 1st solution
# O(1) time | O(1) space
class Solution:
    def pivotInteger(self, n: int) -> int:
        t = n * (n + 1) // 2
        x = int(math.sqrt(t))
        if x * x == t:
            return x
        return -1
