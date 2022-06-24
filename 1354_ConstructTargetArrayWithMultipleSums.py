# 1st solution
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-num for num in target]
        heapify(heap)
        total = sum(target)
        while True:
            largest = -heappop(heap)
            if largest == 1: return True
            if total == largest: return False
            total -= largest
            cand = (largest - 1) % total + 1
            if cand == largest: return False
            total += cand
            heappush(heap, -cand)