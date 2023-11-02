# 1st solution
# O(n) time | O(n) space
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parseEquation(s):
            coef, const = 0, 0
            if s[0] in "+-":
                s = "0+0" + s + "+"
            else:
                s = "0+" + s + "+"
            sign = 1
            lastSign = 1
            # print(s)
            for i in range(2, len(s)):
                ch = s[i]
                # print(i, ch)
                if ch == "x":
                    # print(lastSign, i, s[lastSign+1:i])
                    if i > lastSign + 1:
                        num = int(s[lastSign+1:i])
                    else:
                        num = 1
                    coef += sign * num
                elif ch == "+":
                    if "x" not in s[lastSign+1:i]:
                        num = int(s[lastSign+1:i])
                        const += sign * num
                    sign = 1
                    lastSign = i
                elif ch == "-":
                    if "x" not in s[lastSign+1:i]:
                        num = int(s[lastSign+1:i])
                        const += sign * num
                    sign = -1
                    lastSign = i
            return coef, const
        
        leftEquation, rightEquation = equation.split("=")
        leftCoef, leftConst = parseEquation(leftEquation)
        rightCoef, rightConst = parseEquation(rightEquation)

        coef = leftCoef - rightCoef
        const = rightConst - leftConst
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={const // coef}"

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def solveEquation(self, equation: str) -> str:
        def parseEquation(s):
            s = s.replace("-", "+-").replace("-x", "-1x")
            stack = s.split("+")
            coef, const = 0, 0
            for ch in stack:
                if len(ch) == 0:
                    continue

                if ch[-1] == "x":
                    t = ch[:-1]
                    if len(t) == 0:
                        coef += 1
                    else:
                        coef += int(t)
                else:
                    const += int(ch)
                    
            return coef, const
        
        leftEquation, rightEquation = equation.split("=")
        leftCoef, leftConst = parseEquation(leftEquation)
        rightCoef, rightConst = parseEquation(rightEquation)

        coef = leftCoef - rightCoef
        const = rightConst - leftConst
        
        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={const // coef}"