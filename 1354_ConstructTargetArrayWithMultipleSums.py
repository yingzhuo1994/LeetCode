# 1st solution
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = []
        for num in target: heappush(heap, -num)
        s = sum(target)
        while True:
            elem = -heappop(heap)
            if elem == 1: return True
            if s == elem: return False
            cand = (elem - 1) % (s - elem) + 1
            if cand == elem: return False
            s = s - elem + cand
            heappush(heap, -cand)