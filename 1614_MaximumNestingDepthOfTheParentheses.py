# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxDepth(self, s: str) -> int:
        left = 0
        ans = 0
        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                left -= 1
            ans = max(ans, left)
        return ans