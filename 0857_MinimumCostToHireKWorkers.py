# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = [[w/q, q] for w, q in zip(wage, quality)]
        workers.sort()

        totalQuality = 0
        minHeap = []
        for i in range(k):
            heappush(minHeap, -workers[i][1])
            totalQuality += workers[i][1]
        
        ans = totalQuality * workers[k-1][0]
        
        for i in range(k, len(workers)):
            totalQuality += heappop(minHeap)
            totalQuality += workers[i][1]
            heappush(minHeap, -workers[i][1])
            curCost = totalQuality * workers[i][0]
            ans = min(ans, curCost)
        return ans