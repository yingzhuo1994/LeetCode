# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        while start > 0 or goal > 0:
            if not (start & 1) == (goal & 1):
                ans += 1
            start >>= 1
            goal >>= 1
        return ans