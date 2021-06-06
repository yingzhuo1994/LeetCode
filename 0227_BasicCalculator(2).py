class Solution:
    def calculate(self, s: str) -> int:
        # 1st solution
        # O(n) time | O(n) space
        n = len(s)
        if n == 0:
            return 0
        stack = []
        curNum = 0
        operation = '+'
        for i in range(n):
            ch = s[i]
            print(ch, curNum, operation, stack)
            if ch.isdigit():
                curNum = (curNum * 10) + int(ch)
            if ch in '+-*/' or i == n-1:
                if operation == '-':
                    stack.append(-curNum)
                elif operation == '+':
                    stack.append(curNum)
                elif operation == '*':
                    stackTop = stack.pop()
                    stack.append(stackTop * curNum)
                elif operation == '/':
                    stackTop = stack.pop()
                    stack.append(int(stackTop / curNum))
                operation = ch
                curNum = 0
        return sum(stack)     