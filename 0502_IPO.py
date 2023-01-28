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