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


# 2nd solution
# O(mn) time | O(mn) space
class Solution:
    def findFarmland(self, land: "List[List[int]]") -> "List[List[int]]":
        m, n, res = len(land), len(land[0]), []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    r, c = i, j
                    ## 题目确保农场相互独立
                    while c < n - 1 and land[i][c + 1] == 1:
                        c += 1
                    while r < m - 1 and land[r + 1][j] == 1:
                        r += 1
                    res.append([i, j, r, c])

                    ## 退耕还林
                    for n1 in range(i, r + 1):
                        for n2 in range(j, c + 1):
                            land[n1][n2] = 0
                    
        return res