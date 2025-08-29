# 1st solution
# O(n) time | O(1) space
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        diag = -1
        for a, b in dimensions:
            s = a**2 + b**2
            if s > diag:
                diag = s
                ans = a * b
            elif s == diag:
                ans = max(ans, a * b)
        return ans 