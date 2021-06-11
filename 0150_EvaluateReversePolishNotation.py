class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1st solution
        # O(n) time | O(1) space
        stack = []
        for ch in tokens:
            if ch not in '+-*/':
                stack.append(int(ch))
            else:
                lastNum = stack.pop()
                if ch == '+':
                    stack[-1] += lastNum
                elif ch == '-':
                    stack[-1] -= lastNum
                elif ch == '*':
                    stack[-1] *= lastNum
                elif ch == '/':
                    stack[-1] = int(stack[-1] / lastNum)
        return stack.pop()