# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        largest = max(piles)
        if n == h:
            return max(piles)

        smallest = 1

        while smallest < largest:
            middle = smallest + (largest - smallest) // 2
            if self.isEnough(piles, h, middle):
                largest = middle
            else:
                smallest = middle + 1
        return smallest
    
    def isEnough(self, piles, h, k):
        count = 0
        for pile in piles:
            count += (pile + k - 1) // k
        return count <= h