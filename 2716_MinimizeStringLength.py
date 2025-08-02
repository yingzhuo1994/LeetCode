# 1st solution
# O(n) time | O(1) space
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))