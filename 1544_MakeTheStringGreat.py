# 1st solution
# O(n) time | (n) space
class Solution:
    def makeGood(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch.lower() == stack[-1].lower() and ch != stack[-1]:
                stack.pop()
            else:
                stack.append(ch)
        return "".join(stack)