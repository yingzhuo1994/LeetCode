# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, s: str) -> int:
        first = 0
        second = 0
        for i, ch in enumerate(s):
            if i & 1:
                if ch == "1":
                    second += 1
                else:
                    first += 1
            else:
                if ch == "1":
                    first += 1
                else:
                    second += 1
        return min(first, second)