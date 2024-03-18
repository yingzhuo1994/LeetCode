# 1st solution
# O(n) time | O(1) space
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal + goal)