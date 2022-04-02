# O(log(x)) time | O(1) space
class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        value = abs(x)
        while value != 0:
            lastNum = value % 10
            num = num * 10 + lastNum
            value = value // 10

        # Pay attention to the integer range [-2^31, 2^31 - 1]
        if x < 0 and num <= 2**31:
            return -num
        elif x > 0 and num < 2**31:
            return num
        else:
            return 0


