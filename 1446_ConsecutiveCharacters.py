# O(n) time | O(1) space
class Solution:
    def maxPower(self, s: str) -> int:
        ch = ""
        count = 0
        ans = 1
        for i in range(len(s)):
            if s[i] == ch:
                count += 1
                ans = max(ans, count)
            else:
                ch = s[i]
                count = 1
        return ans