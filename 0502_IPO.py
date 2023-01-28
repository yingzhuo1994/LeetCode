class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:       
        minHeap = []
        maxHeap = []
        for p, c in zip(profits, capital):
            if c <= w:
                heappush(minHeap, [-p, c])
            else:
                heappush(maxHeap, [c, -p])
        
        i = 0
        while i < k and minHeap:
            p, _ = heappop(minHeap)
            p = -p
            w += p
            while maxHeap and maxHeap[0][0] <= w:
                c, p = heappop(maxHeap)
                heappush(minHeap, [p, c])
            i += 1
        return w

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()
        # heapq is a min heap, but we need a max heap
        # so we will store negated elements
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                # push a negated element
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break
            # pop a negated element
            w += -heappop(q)
        return w