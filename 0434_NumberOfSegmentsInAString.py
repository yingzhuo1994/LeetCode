# 1st solution
# O(n) time | O(1) space
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        last = " "
        for ch in s:
            if ch != " " and last == " ":
                count += 1
            last = ch
        return count
