# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacificOcean = [[False for _ in range(n)] for _ in range(m)]
        atlanticOcean = [[False for _ in range(n)] for _ in range(m)]
        nebs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        level = deque()
        for j in range(n):
            pacificOcean[0][j] = True
            level.append([0, j])
        
        for i in range(1, m):
            pacificOcean[i][0] = True
            level.append([i, 0])
        
        while level:
            i, j = level.popleft()
            for dx, dy in nebs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and heights[i][j] <= heights[x][y] and not pacificOcean[x][y]:
                    pacificOcean[x][y] = True
                    level.append([x, y])
        
        level = deque()
        for j in range(n):
            atlanticOcean[m-1][j] = True
            level.append([m-1, j])
        
        for i in range(m-1):
            atlanticOcean[i][n-1] = True
            level.append([i, n-1])
        
        while level:
            i, j = level.popleft()
            for dx, dy in nebs:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and heights[i][j] <= heights[x][y] and not atlanticOcean[x][y]:
                    atlanticOcean[x][y] = True
                    level.append([x, y])
        
        ans = []
        for i in range(m):
            for j in range(n):
                if pacificOcean[i][j] and atlanticOcean[i][j]:
                    ans.append([i, j])
        
        return ans