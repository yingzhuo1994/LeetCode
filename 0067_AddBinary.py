# 1st solution
# O(n) time | O(n) space
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        s1 = a[::-1]
        s2 = b[::-1]
        carry = 0
        for i in range(max(len(s1), len(s2))):
            num1 = int(s1[i]) if i < len(s1) else 0
            num2 = int(s2[i]) if i < len(s2) else 0
            num = num1 + num2 + carry
            carry = num // 2
            result.append(num % 2)
        if carry == 1:
            result.append(1)
        return "".join([str(result[i]) for i in reversed(range(len(result)))])