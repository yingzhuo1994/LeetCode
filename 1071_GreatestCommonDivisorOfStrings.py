# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while a > 0:
                a, b = b % a, a
            return b
        
        m, n = len(str1), len(str2)
        k = gcd(m, n)

        for i in reversed(range(1, k + 1)):
            if k % i != 0:
                continue
            x, y = m // i, n // i
            if str1[:i] * x == str1 and str1[:i] * y == str2:
                return str1[:i]
        return ""

# 2nd solution
# O(m + n) time | O(m + n) space
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while a > 0:
                a, b = b % a, a
            return b
        if str1 + str2 != str2 + str1:
            return ""
        m, n = len(str1), len(str2)
        k = gcd(m, n)

        return str1[:k]

# 3rd solution
# O(n^2) time | O(n^2) space
# where n = max(len(str1), len(str2))
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''