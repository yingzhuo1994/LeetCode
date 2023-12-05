# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n & 1:
                n //= 2
                ans += n
                n += 1
            else:
                n //= 2
                ans += n
        return ans