# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        start = 0
        prev = -1
        ans = 1
        for i, ch in enumerate(s):
            if prev < 0 or ord(ch) - 1 == prev:
                ans = max(ans, i - start + 1)
            else:
                start = i
            prev = ord(ch)
        return ans