# 1st solution
# O(n*log(n)) time | O(1) space
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        smallest = total // h
        if smallest == 0:
            return 1
        largest = max(piles)
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
            q, r = pile // k, pile % k
            if r == 0:
                count += q
            else:
                count += q + 1
        return count <= h