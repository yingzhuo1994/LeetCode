# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        minHeap = []
        ans = 0
        for i, apple in enumerate(apples):
            heappush(minHeap, [i + days[i], min(apple, days[i])])
            while minHeap and minHeap[0][0] <= i:
                heappop(minHeap)
            if minHeap:
                ans += 1
                if minHeap[0][1] > 1:
                    minHeap[0][1] -= 1
                else:
                    heappop(minHeap)
        i = n
        while minHeap:
            t, apple = heappop(minHeap)
            if t <= i:
                continue
            else:
                diff = t - i
                ans += min(diff, apple)
                i += min(diff, apple)
        return ans  
