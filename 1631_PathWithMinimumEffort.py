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
                if 0 <= x < m and 0 <= y < n:
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
        
        def dfs(LIMIT, x, y, visited):
            visited.add((x, y)) 
            for dx, dy in neibs:
                i = x + dx
                j = y + dy
                if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                    if abs(heights[x][y] - heights[i][j]) <= LIMIT:
                        if dfs(LIMIT, i, j, visited):
                            return True
            return (m - 1, n - 1) in visited
        
        beg, end = -1, max(max(heights, key=max))
        while beg + 1 < end:
            mid = (beg + end) // 2
            visited = set()
            if dfs(mid, 0, 0, visited):
                end = mid
            else:
                beg = mid
                
        return end

# 3rd solution, Dijikstra
# O(ElogV) = O(mn * log(mn)) time | O(mn) space
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        dist = [[math.inf] * n for _ in range(m)]
        dist[0][0] = 0
        minHeap = [(0, 0, 0)] # distance, row, col
        DIR = [0, 1, 0, -1, 0]

        while minHeap:
            d, r, c = heappop(minHeap)
            if d > dist[r][c]: 
                continue  # this is an outdated version -> skip it
            if r == m - 1 and c == n - 1:
                return d  # Reach to bottom right
            
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i+1]
                if 0 <= nr < m and 0 <= nc < n:
                    newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > newDist:
                        dist[nr][nc] = newDist
                        heappush(minHeap, (dist[nr][nc], nr, nc))