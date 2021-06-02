class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1st solution
        # O(n) time | O(1) space
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                else:
                    stack.append(int(l / r))
        return stack.pop()
