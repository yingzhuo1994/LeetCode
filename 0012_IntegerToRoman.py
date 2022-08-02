# 1st solution
# O(1) time | O(1) space
class Solution:
    def intToRoman(self, num: int) -> str:
        stack = []
        while num > 0:
            if num >= 1000:
                num -= 1000
                stack.append("M")
            elif num >= 900:
                num -= 900
                stack.append("CM")
            elif num >= 500:
                num -= 500
                stack.append("D")
            elif num >= 400:
                num -= 400
                stack.append('CD')
            elif num >= 100:
                num -= 100
                stack.append("C")
            elif num >= 90:
                num -= 90
                stack.append("XC")
            elif num >= 50:
                num -= 50
                stack.append("L")
            elif num >= 40:
                num -= 40
                stack.append("XL")
            elif num >= 10:
                num -= 10
                stack.append("X")
            elif num >= 9:
                num -= 9
                stack.append("IX")
            elif num >= 5:
                num -= 5
                stack.append("V")
            elif num >= 4:
                num -= 4
                stack.append("IV")
            else:
                num -= 1
                stack.append("I")
        return "".join(stack)

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def intToRoman(self, num: int) -> str:
        def digit(a,b,c,dig):
            return ["",a,2*a,3*a,a+b,b,b+a,b+2*a,b+3*a,a+c][dig]
        
        l = ["I","V","X","L","C","D","M","!","!"]
        out, i = "", 0

        while num > 0:
            num, last = divmod(num, 10)
            out = digit(l[i], l[i+1], l[i+2], last) + out
            i += 2
        return out