# O(n) time | O(n) space
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        stack = []
        n, r = columnNumber, 0
        while n > 0:
            r = (n - 1) % 26 + 1
            n = (n - r) // 26
            ch = chr(ord("A") - 1 + r)
            stack.append(ch)
        stack.reverse()
        return "".join(stack)

