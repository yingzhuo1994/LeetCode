# 1st solution
# O(n) time | O(n) space
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    if stack[-1] != "(":
                        stack[-1] += 1
                    else:
                        stack.append(1)
                else:
                    num = stack.pop()
                    stack.pop()
                    num = num * 2
                    while len(stack) > 0 and stack[-1] != "(":
                        num += stack.pop()
                    stack.append(num)

        return stack[0]