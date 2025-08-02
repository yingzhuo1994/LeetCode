# 1st solution
# O(n) time | O(1) space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = 0
        ans = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    ans += 1
        ans += left
        return ans