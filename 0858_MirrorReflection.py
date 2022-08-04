# 1st solution
# O(1) time | O(1) space
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        return (q//gcd(p,q)%2 - p//gcd(p,q)%2 + 1)

# 2nd solution
# O(1) time | O(1) space
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0: 
            p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2

# 3rd solution
# O(1) time | O(1) space
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        return ((p & -p) >= (q & -q)) + ((p & -p) > (q & -q))