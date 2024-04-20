# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j, loc):
            if visited[i][j]:
                return
            visited[i][j] = True
            if i < loc[0]:
                loc[0] = i
            if j < loc[1]:
                loc[1] = j
            if i > loc[2]:
                loc[2] = i
            if j > loc[3]:
                loc[3] = j
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and land[x][y] == 1:
                    dfs(x, y, loc)
        ans = []
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                if land[i][j] == 1:
                    loc = [i, j, i, j]
                    dfs(i, j, loc)
                    ans.append(loc)
        return ans