# 1st solution
# O(n) time | O(n) space
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        stack = []
        curNum = 0
        operation = '+'
        for i in range(n):
            ch = s[i]
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

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def calculate(self, s: str) -> int:
        front, back = 0, 0
        curNum = 0
        operation = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                curNum = (curNum * 10) + int(ch)
            if ch in '+-*/' or i == len(s) - 1:
                if operation == '-':
                    front, back = front + back, -curNum
                elif operation == '+':
                    front, back = front + back, curNum
                elif operation == '*':     
                    back = back * curNum
                elif operation == '/':
                    back = int(back / curNum)
                operation = ch
                curNum = 0
        return front + back