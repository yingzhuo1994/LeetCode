# 1st solution, dfs
# O(n^2) time | O(n^2) space
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n, ans = len(bombs), 0
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i == j: continue
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                if (r1)**2 >= (x2 - x1)**2 + (y2 - y1)**2:
                    graph[i].append(j)
        
        
        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = set([i])
            dfs(i, visited)
            ans = max(ans, len(visited))
                          
        return ans

# 2nd solution, bfs
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        
        def bfs(node, visited):

            stack = [node]
            visited.add(node)
            while stack:
                idx = stack.pop()
                x1, y1, r1 = bombs[idx]
                for i in range(n):
                    if i in visited:
                        continue
                    x2, y2, r2 = bombs[i]
                    if r1**2 >= (x2 - x1)**2 + (y2 - y1)**2:
                        visited.add(i)
                        stack.append(i)
            return len(visited)
        ans = 1
        for i in range(n):
            visited = set()
            ans = max(ans, bfs(i, visited))
        return ans