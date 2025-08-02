# 1st solution
# O(mn * log(m)) time | O(m) space
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m = len(values)
        n = len(values[0])
        minHeap = []
        for i in range(m):
            heappush(minHeap, [values[i][n-1], i, n - 1])
        cost = 0
        for d in range(1, m * n + 1):
            val, i, j = heappop(minHeap)
            cost += val * d
            if j > 0:
                heappush(minHeap, [values[i][j-1], i, j - 1])
        return cost
