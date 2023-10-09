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

# 2nd solution
# O(n) time | O(n) sapce
class Solution:
    def splitNum(self, num: int) -> int:
        count = [0 for _ in range(11)]
        while num > 0:
            d = num % 10
            num //= 10
            count[d] += 1
        
        n = sum(count)
        for i in range(1, 10):
            count[i] += count[i - 1]
        stack = [0 for _ in range(n)]
        for i in reversed(range(10)):
            stack[count[i - 1]:count[i]] = [str(i)] * (count[i] - count[i - 1])

        num1 = "".join(stack[0::2])
        num2 = "".join(stack[1::2])

        num1 = int(num1)
        num2 = int(num2)
        return  num1 + num2