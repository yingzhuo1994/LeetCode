# 1st solution
class Solution:
    @cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        
        ans = float("inf")
        if len(s1) > 0:
            ans = min(ans, ord(s1[0]) + self.minimumDeleteSum(s1[1:], s2))
        if len(s2) > 0:
            ans = min(ans, ord(s2[0]) + self.minimumDeleteSum(s1, s2[1:]))
        if s1 and s2 and s1[0] == s2[0]:
            ans = min(ans, self.minimumDeleteSum(s1[1:], s2[1:]))
        
        return ans