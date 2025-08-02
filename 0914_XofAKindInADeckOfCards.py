# 1st solution
# O(n) time | O(n) space
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a
        cnt = Counter(deck)
        g = reduce(gcd, cnt.values())
        return g > 1