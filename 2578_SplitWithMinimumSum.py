# 1st solution
# O(n * log(n)) time | O(n) sapce
class Solution:
    def splitNum(self, num: int) -> int:
        stack = [ch for ch in str(num)]
        stack.sort()
        num1 = "".join(stack[0::2])
        num2 = "".join(stack[1::2])

        num1 = int(num1)
        num2 = int(num2)
        return  num1 + num2