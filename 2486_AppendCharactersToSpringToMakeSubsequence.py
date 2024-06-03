# 1st solution
# O(n) time | O(1) space
# n = len(s)
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for ch in s:
            if ch == t[j]:
                j += 1
            if j == len(t):
                break
        return len(t) - j
