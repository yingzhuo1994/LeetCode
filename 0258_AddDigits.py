# 1st solution
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

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        res = num % 9
        if res == 0:
            return 9
        return res