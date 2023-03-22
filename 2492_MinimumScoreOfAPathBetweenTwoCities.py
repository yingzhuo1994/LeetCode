# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n  +1)]
        for a, b, dist in roads:
            graph[a].append([b, dist])
            graph[b].append([a, dist])
        
        visited =set()
        self.score = float("inf")
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neigh, dist in graph[node]:
                self.score = min (self.score, dist)
                dfs(neigh)
        
        dfs(1)
        return self.score
