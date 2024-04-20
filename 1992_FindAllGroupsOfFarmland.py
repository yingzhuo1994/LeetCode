# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        def dfs(i, j, loc):
            if land[i][j] <= 0:
                return
            land[i][j] = -1
 
            loc[0] = min(loc[0], i)
            loc[1] = min(loc[1], j)
            loc[2] = max(loc[2], i)
            loc[3] = max(loc[3], j)

            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and land[x][y] == 1:
                    dfs(x, y, loc)
        ans = []
        for i in range(m):
            for j in range(n):
                if land[i][j] <= 0:
                    continue
                if land[i][j] == 1:
                    loc = [i, j, i, j]
                    dfs(i, j, loc)
                    ans.append(loc)
        return ans