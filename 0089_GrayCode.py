# 1st solution, TLE
# O(2^n) time | O(n) space
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        t = self.grayCode(n-1)
        return t + [i+(1<<(n-1)) for i in t][::-1]