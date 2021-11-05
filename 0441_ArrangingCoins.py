class Solution:
    # 1st solution
    # O(1) time | O(1) space
    def arrangeCoins(self, n: int) -> int:
        return int((sqrt(8* n + 1) - 1)/2.0)

    # 2nd solution
    # O(n^0.5) time | O(1) space
    def arrangeCoins(self, n: int) -> int:
        k = 0
        while n >= 0:
            k += 1
            n -= k
        return k-1