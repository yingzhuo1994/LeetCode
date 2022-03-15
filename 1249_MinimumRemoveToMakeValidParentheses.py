# 1st solution
# O(n) time | O(n) space
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        leftParen = []
        for i, ch in enumerate(s):
            stack.append(ch)
            if ch == "(":
                leftParen.append(i)
            elif ch == ")":
                if len(leftParen) > 0:
                    leftParen.pop()
                else:
                    stack[i] = ""
        for idx in leftParen:
            stack[idx] = ""
        return "".join(stack)