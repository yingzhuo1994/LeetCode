# 1st solution
# O(n) time | O(n) space
class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isdigit():
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)