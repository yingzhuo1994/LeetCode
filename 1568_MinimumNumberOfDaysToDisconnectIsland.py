# 1st solution
# O((mn)^2) time | O(mn) space
class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        graph = {}
        def getIdx(i, j):
            return i * n + j
        def dfs(i, j):
            idx = getIdx(i, j)
            if idx not in graph:
                graph[idx] = []
            grid[i][j] = -1
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 0:
                    newIdx = getIdx(x, y)
                    if newIdx not in graph:
                        graph[newIdx] = []
                    graph[idx].append(newIdx)
                    if grid[x][y] == 1:
                        dfs(x, y)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j)
        land = len(graph)
        if land == 0:
            return 0
        degree = [[idx, len(graph[idx])] for idx in graph]
        # degree.sort(key=lambda v: v[1])
        visited = set()
        def dfs2(idx):
            if idx in visited:
                return
            visited.add(idx)
            for neig in graph[idx]:
                dfs2(neig)
        dfs2(degree[0][0])
        if len(visited) != land:
            return 0
        levels = {d: [] for d in range(5)}
        for idx, d in degree:
            levels[d].append(idx)
        if len(levels[1]) == 1 or len(graph) == 1:
            return 1
        # print(graph)
        for i in range(len(degree)):
            idx = degree[i][0]
            visited = set([idx])
            if i + 1 < len(degree):
                dfs2(degree[i+1][0])
            else:
                dfs2(degree[i-1][0])
            if len(visited) != land:
                return 1
        return 2
        