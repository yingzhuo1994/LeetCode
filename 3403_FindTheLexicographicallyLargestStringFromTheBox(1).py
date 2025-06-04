# 1st solution
# O(n * (n - k)) time | O(n - k) space
class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1:
            return s
        n = len(s)
        return max(s[i: i + n - k + 1] for i in range(n))