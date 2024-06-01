# 1st solution
# O(n) time | O(1) space
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score