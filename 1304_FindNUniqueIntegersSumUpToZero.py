# 1st solution
# O(n) time | O(n) space
class Solution:
    def sumZero(self, n: int) -> List[int]:
        k = n >> 1
        ans = [-i for i in range(1, k + 1)] + [i for i in range(1, k + 1)]
        if n & 1:
            ans.append(0)
        return ans
            