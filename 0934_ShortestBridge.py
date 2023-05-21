# 1st solution, TLE
# O(n^4) time | O(n^2) space
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j, lst):
            if grid[i][j] == 1:
                lst.append([i, j])
                grid[i][j] = -1
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        dfs(x, y, lst)
        
        lst1 = []
        lst2 = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if len(lst1) == 0:
                        dfs(i, j, lst1)
                    else:
                        dfs(i, j, lst2)
        
        ans = float("inf")
        for x0, y0 in lst1:
            for x1, y1 in lst2:
                dist = abs(x1 - x0) + abs(y1 - y0) - 1
                ans = min(ans, dist)
        
        return ans

# 2nd solution
# O(n^2) time | O(n^2) space
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j, lst):
            if grid[i][j] == 1:
                lst.append([i, j])
                grid[i][j] = -1
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        dfs(x, y, lst)
        
        def getBorders(lst, borders):
            for i, j in lst:
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        borders.append([i, j])
            return borders

        
        lst1 = []
        lst2 = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if len(lst1) == 0:
                        dfs(i, j, lst1)
                    else:
                        dfs(i, j, lst2)
        
        border1 = []
        border2 = []
        getBorders(lst1, border1)
        getBorders(lst2, border2)

        ans = float("inf")
        for x0, y0 in border1:
            for x1, y1 in border2:
                dist = abs(x1 - x0) + abs(y1 - y0) - 1
                ans = min(ans, dist)
        
        return ans

# 3rd solution
# O(n^2) time | O(n^2) space
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        neighbors = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        def dfs(i, j, lst):
            if grid[i][j] == 1:
                lst.append([i, j])
                grid[i][j] = -1
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        dfs(x, y, lst)
        
        def getBorders(lst, borders):
            for i, j in lst:
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        borders.add((i, j))
            return borders

        
        lst1 = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if len(lst1) == 0:
                        dfs(i, j, lst1)

        level = set()
        getBorders(lst1, level)

        ans = 0
        while level:
            newLevel = set()
            for i, j in level:
                for dx, dy in neighbors:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 0:
                            grid[x][y] = -2
                            newLevel.add((x, y))
                        elif grid[x][y] == 1:
                            return ans
            level = newLevel
            ans += 1
        
        return -1