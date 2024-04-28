# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def baseNeg2(self, n: int) -> str:
        res = []
        while n:
            res.append(n & 1)
            n = -(n >> 1)
        return "".join(map(str, res[::-1] or [0]))
    
    def base2(self, x):
        res = []
        while x:
            res.append(x & 1)
            x = x >> 1
        return "".join(map(str, res[::-1] or [0]))