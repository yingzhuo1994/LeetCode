# 1st solution
# O(n) time | O(1) space
class Solution:
    def countKeyChanges(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            if s[i-1].lower() != s[i].lower():
                ans += 1
        return ans