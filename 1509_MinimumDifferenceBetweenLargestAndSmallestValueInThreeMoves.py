# 1st solution
# O(n) time | O(1) space
class Solution:
    def minDifference(self, nums: List[int]) -> int:        
        maxHeap = []
        minHeap = []
        for i, num in enumerate(nums):
            heappush(minHeap, [num, i])
            heappush(maxHeap, [-num, i])
            if len(minHeap) > 4:
                heappop(minHeap)
            if len(maxHeap) > 4:
                heappop(maxHeap)
        values = minHeap + [[-val, idx] for val, idx in maxHeap]
        values.sort()
        candidates = [values[0]]
        for i in range(1, len(values)):
            if values[i][1] == candidates[-1][1]:
                continue
            else:
                candidates.append(values[i])

        if len(candidates) <= 4:
            return 0
        ans = float("inf")
        for a in range(4):
            b = 3 - a
            diff = candidates[len(candidates) - 1 - b][0] - candidates[a][0]
            ans = min(ans, diff)
        return ans