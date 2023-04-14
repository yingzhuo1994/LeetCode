# 1st solution
# O(n) time | O(n) space
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        candySet = set(candyType)
        k = len(candySet)
        return min(k, n // 2)