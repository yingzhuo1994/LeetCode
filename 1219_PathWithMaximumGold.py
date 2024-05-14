# 1st solution
# O(m^2 * n^ 2) time | O(mn) space
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        k = m * n
        graph = [[] for _ in range(k)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                node = i * n + j
                if i + 1 < m and grid[i+1][j] > 0:
                    neig = (i + 1) * n + j
                    graph[node].append(neig)
                    graph[neig].append(node)
                if j + 1 < n and grid[i][j + 1] > 0:
                    neig = node + 1
                    graph[node].append(neig)
                    graph[neig].append(node)

        self.ans = 0
        def dfs(node, visited):
            if node in visited:
                return 0
            visited.add(node)
            i, j = divmod(node, n)
            if grid[i][j] == 0:
                return 0
            val = 0
            for neig in graph[node]:
                val = max(val, dfs(neig, visited))
            visited.remove(node)
            return val + grid[i][j]
            
        for node in range(k):
            val = dfs(node, set())
            self.ans = max(self.ans, val)
        
        return self.ans
