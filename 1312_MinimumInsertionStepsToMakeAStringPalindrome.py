# 1st solution
class Solution:
    @cache
    def minInsertions(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        if s[0] == s[-1]:
            return self.minInsertions(s[1:-1])
        left = self.minInsertions(s[1:])
        right = self.minInsertions(s[:-1])
        ans = min(left, right) + 1
        return ans