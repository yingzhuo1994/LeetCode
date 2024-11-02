# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        ans = 0
        while n > 0 or k > 0:
            if (n & 1) != (k & 1):
                if n & 1:
                    ans += 1
                else:
                    return -1
            n >>= 1
            k >>= 1
        return ans