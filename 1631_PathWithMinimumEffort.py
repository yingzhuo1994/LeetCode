# 1st solution
# O(mn*log(mn)) time | O(mn) space
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        efforts = [[float("inf") for _ in range(n)] for _ in range(m)]
        efforts[0][0] = 0
        minHeap = [(0, 0, 0)]
        while minHeap:
            curEffort, i, j = heappop(minHeap)
            if (i, j) == (m - 1, n - 1):
                break
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

# 2nd solution
# O(mn*log(H)) time | O(mn) space
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        neibs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        def dfs(LIMIT, x, y):
            visited.add((x, y)) 
            for dx, dy in neibs:
                if 0<=dx+x<m and 0<=dy+y<n and (dx+x, dy+y) not in visited:
                    if abs(heights[x][y] - heights[dx+x][dy+y]) <= LIMIT:
                        dfs(LIMIT, dx+x, dy+y)
        
        beg, end = -1, max(max(heights, key=max))
        while beg + 1 < end:
            mid = (beg + end)//2
            visited = set()
            dfs(mid, 0, 0)
            if (m - 1, n - 1) in visited:
                end = mid
            else:
                beg = mid
                
        return end