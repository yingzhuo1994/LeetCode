# 1st solution
# O(n) time | O(1) space
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        a = 0
        for i in range(n//2):
            if s[i] in vowels:
                a += 1
        b = 0
        for i in range(n//2, n):
            if s[i] in vowels:
                b += 1
        return a == b