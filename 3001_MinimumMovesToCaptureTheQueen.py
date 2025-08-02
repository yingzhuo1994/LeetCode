# 1st solution
# O(1) time | O(1) space
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if a == c and min(b, f) < d < max(b, f):
                pass
            else:
                return 1
        if b == f:
            if b == d and min(a, e) < c < max(a, e):
                pass
            else:
                return 1
        if d - c == f - e:
            if d - c == b - a and min(c, e) < a < max(c, e):
                pass
            else:
                return 1
        if d + c == f + e:
            if d + c == a + b and min(c, e) < a < max(c, e):
                pass
            else:
                return 1
        return 2
        