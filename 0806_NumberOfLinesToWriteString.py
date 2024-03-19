# 1st solution
# O(n) time | O(1) space
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curWidth = 0
        for i in range(len(s)):
            width = widths[ord(s[i]) - ord("a")]
            if curWidth + width > 100:
                lines += 1
                curWidth = width
            else:
                curWidth += width
        return [lines, curWidth]