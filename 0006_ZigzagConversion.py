# 1st solution
# O(n) time | O(n) space
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        stack = []
        k = numRows
        for i in range(0, len(s), 2 * k - 2):
            stack.append(s[i])
        for i in range(1, k - 1):
            for a in range(i, len(s), 2 * k - 2):
                stack.append(s[a])
                b = a + 2 * (k - 1 - a % (2 * k - 2))
                if b < len(s):
                    stack.append(s[b])
        for i in range(k - 1, len(s), 2 * k - 2):
            stack.append(s[i])
        return "".join(stack)