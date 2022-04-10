# 1st solution
# O(n) time | O(n) space
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                if op[0] == "-":
                    stack.append(-int(op[1:]))
                else:
                    stack.append(int(op))
        return sum(stack)