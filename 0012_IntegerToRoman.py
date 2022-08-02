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