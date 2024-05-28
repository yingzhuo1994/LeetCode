# 1st solution
# O(n) time | O(1) space
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        cost = 0
        ans = 0
        for i, ch in enumerate(s):
            cost += abs(ord(ch) - ord(t[i]))
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            ans = max(ans, i - start + 1)
        return ans