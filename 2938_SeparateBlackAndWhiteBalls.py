# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimumSteps(self, s: str) -> int:
        white = 0
        steps = 0
        for i, ch in enumerate(s):
            if ch == "0":
                steps += i - white
                white += 1
        return steps