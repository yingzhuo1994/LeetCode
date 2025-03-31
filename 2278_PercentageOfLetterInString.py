# 1st solution
# O(n) time | O(1)
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        cnt = s.count(letter)
        return cnt * 100 // n