# 1st solution
# O(kn) time | O(n) space
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        k = len(part)
        for i, ch in enumerate(s):
            stack.append(ch)
            if len(stack) >= len(part) and "".join(stack[-k:]) == part:
                stack = stack[:-k]
        return "".join(stack)