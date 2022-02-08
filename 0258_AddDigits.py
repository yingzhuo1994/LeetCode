# O(1) time | O(1) space
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            cur = 0
            while num > 0:
                cur += num % 10
                num = num // 10
            num = cur
        return num