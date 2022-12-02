# 1st solution
# O(mn) time | O(m + n) space
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n, heap, trapped = len(heightMap), len(heightMap and heightMap[0]), [], 0
        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heightMap[i][0] = -1
            if n > 1:
                heapq.heappush(heap, (heightMap[i][n-1], i, n-1))
                heightMap[i][n-1] = -1

        for j in range(1, n - 1):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heightMap[i][0] = -1
            if m > 1:
                heapq.heappush(heap, (heightMap[m-1][j], m-1, j))
                heightMap[m-1][j] = -1

        while heap:
            h, i, j = heapq.heappop(heap)
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
                    trapped += max(h - heightMap[x][y], 0)
                    heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                    heightMap[x][y] = -1
        return trapped