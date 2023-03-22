# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n  +1)]
        for a, b, dist in roads:
            graph[a].append([b, dist])
            graph[b].append([a, dist])
        
        visited = set()
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

# 2nd solution, bfs
# O(n) time | O(n) space
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n  +1)]
        for a, b, dist in roads:
            graph[a].append([b, dist])
            graph[b].append([a, dist])
        
        visited = set([1])
        score = float("inf")
        level = [1]
        while level:
            newLevel = []
            for node in level:
                for neigh, dist in graph[node]:
                    score = min (score, dist)
                    if neigh not in visited:
                        newLevel.append(neigh)
                        visited.add(neigh)
            level = newLevel
        
        return score