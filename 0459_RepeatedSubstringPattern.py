# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for k in range(1, n // 2 + 1):
            if n % k != 0:
                continue
            sub = s[:k]
            m = n // k
            if sub * m == s:
                return True
        return False

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]