# 1st solution
# O(n) time | O(1) space
class Solution:
    def fractionAddition(self, expression: str) -> str:
        @cache
        def gcd(a, b):
            a = abs(a)
            b = abs(b)
            while a:
                a, b = b % a, a
            return b
        
        ans = [0, 1]

        sign = "+"
        a, b = 0, 1
        i = 0
        while i < len(expression):
            ch = expression[i]
            if ch == "/":
                j = i + 1
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                b = int(expression[i+1:j])
                i = j
            elif ch in "+-":
                if sign == "+":
                    ans[0] = ans[0] * b + ans[1] * a
                else:
                    ans[0] = ans[0] * b - ans[1] * a

                ans[1] = ans[1] * b
                g = gcd(ans[0], ans[1])

                ans[0] //= g
                ans[1] //= g

                a, b = 0, 1
                sign = ch
                i += 1
            else:
                j = i
                while j < len(expression) and expression[j].isdigit():
                    j += 1

                a = int(expression[i:j])
                i = j

        if sign == "+":
            ans[0] = ans[0] * b + ans[1] * a
        else:
            ans[0] = ans[0] * b - ans[1] * a

        ans[1] = ans[1] * b
        g = gcd(ans[0], ans[1])
        ans[0] //= g
        ans[1] //= g

        return str(ans[0]) + "/" + str(ans[1])

