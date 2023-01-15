# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.count = 0

        def dfs(start, node, parent=-1):
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if vals[neigh] > start:
                    continue
                if vals[neigh] == start:
                    self.count += 1
                dfs(start, neigh, node)
        
        for node in range(n):
            dfs(vals[node], node)
        
        self.count //= 2
        return n + self.count