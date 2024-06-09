# 1st solution
# O(n * log(U)) time | O(1) space
# where U = max(piles)
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


# 2nd solution
# O(n * log(U)) time | O(1) space
# where U = max(piles)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        ans = end
        while start <= end:
            mid = start + (end - start) // 2
            t = sum([(pile + mid - 1) // mid for pile in piles])
            if t <= h:
                ans = min(ans, mid)
                end = mid - 1
            else:
                start = mid + 1
        return ans