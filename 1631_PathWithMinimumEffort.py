# 1st solution
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        efforts = [[float("inf") for _ in range(len(heights[0]))] for _ in range(len(heights))]
        efforts[0][0] = 0
        minHeap = [(0, 0, 0)]
        while minHeap:
            curEffort, i, j = heappop(minHeap)
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                    newEffort = abs(heights[x][y] - heights[i][j])
                    nextEffort = max(curEffort, newEffort)
                    if nextEffort < efforts[x][y]:
                        efforts[x][y] = nextEffort
                        heappush(minHeap, (nextEffort, x, y))
        return efforts[-1][-1]