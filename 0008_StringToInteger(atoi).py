class Solution:
    def myAtoi(self, s: str) -> int:
        # O(n) time | O(1) space
        sign = 1
        k = 0
        num = 0
        while k < len(s):
            if s[k] == ' ':
                k += 1
            else:
                break

        if k < len(s):
            if s[k] == '+':
                sign = 1
                k += 1
            elif s[k] == '-':
                sign = -1
                k += 1

        while k < len(s):
            if s[k].isdigit():
                num = 10 * num + int(s[k])
            else:
                break
            k += 1
        if sign > 0:
            return min(num, 2**31 - 1)
        elif sign < 0:
            return sign * min(num, 2**31)
