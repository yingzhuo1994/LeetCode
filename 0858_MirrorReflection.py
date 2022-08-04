# 1st solution
# O(1) time | O(1) space
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        return (q//gcd(p,q)%2 - p//gcd(p,q)%2 + 1)