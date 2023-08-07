# 1st solution
# O(n) time | O(n) space
class Solution:
    def solveEquation(self, equation: str) -> str:
        leftEquation, rightEquation = equation.split("=")

        def getStack(equation):
            start = 0
            stack = []
            for i in range(len(equation)):
                if equation[i] in "+-":
                    num = equation[start:i]
                    if len(num) == 0:
                        num = "0"
                    stack.append(num)
                    stack.append(equation[i])
                    start = i + 1
                elif i == len(equation) - 1:
                    stack.append(equation[start:i+1])
            const = 0
            coef = 0
            lastOp = "+"
            i = 0
            while i <= len(stack):
                if i == len(stack) or stack[i] in "+-":
                    if stack[i - 1][-1] == "x":
                        if len(stack[i -1]) > 1:
                            num = int(stack[i - 1][:-1])
                        else:
                            num = 1
                        if lastOp == "+":
                            coef += num
                        else:
                            coef -= num
                    else:
                        num = int(stack[i - 1])
                        if lastOp == "+":
                            const += num
                        else:
                            const -= num
                    if i < len(stack):
                        lastOp = stack[i]
                i += 1

            return coef, const
        
        leftCoef, leftConst = getStack(leftEquation)
        rightCoef, rightConst = getStack(rightEquation)

        coef = leftCoef - rightCoef
        const = rightConst - leftConst
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={const // coef}"