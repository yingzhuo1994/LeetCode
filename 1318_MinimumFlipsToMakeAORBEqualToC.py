# 1st solution
# O(1) time | O(1) space
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
        while a > 0 or b > 0 or c > 0:
            if c & 1:
                if not (a & 1) and not (b & 1):
                    count += 1
            else:
                if a & 1:
                    count += 1
                if b & 1:
                    count += 1
            a >>= 1
            b >>= 1
            c >>= 1
        
        return count