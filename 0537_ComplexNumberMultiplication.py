# 1st soluton
# O(1) time | O(1) space
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def getComplexNumber(num):
            lst = num.split("+")
            real = int(lst[0])
            img = int(lst[1][:-1])
            return real, img
        
        def complexMultiply(num1, num2):
            real = num1[0] * num2[0] - num1[1] * num2[1]
            img = num1[0] * num2[1] + num1[1] * num2[0]
            return real, img
        
        def transformToString(real, img):
            return str(real) + "+" + str(img) + "i"
        
        num1 = getComplexNumber(num1)
        num2 = getComplexNumber(num2)
        real, img = complexMultiply(num1, num2)
        ans = transformToString(real, img)
        return ans