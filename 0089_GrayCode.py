# 1st solution, recursion
# O(2^n) time | O(n) space
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1: return [0, 1]
        k = n - 1
        last = self.grayCode(k)
        new = [num | (1<<(k)) for num in last]
        new.reverse()
        return last + new

# 2nd solution, iteration
# O(2^n) time | O(n) space
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0, 1]
        for k in range(1, n):
            new = [num | (1<<(k)) for num in ans]
            new.reverse()
            ans += new
        return ans