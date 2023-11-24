# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        k = n // 3
        return sum(piles[k:n-1:2])