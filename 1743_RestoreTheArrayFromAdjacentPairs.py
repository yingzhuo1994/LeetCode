# 1st solution
# O(n) time | O(n) space
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = {}
        for a, b in adjacentPairs:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[a].append(b)
            graph[b].append(a)
        
        ends = [node for node in graph if len(graph[node]) == 1]
        def dfs(node, visited):
            if node in visited:
                return
            ans.append(node)
            visited.add(node)
            for neig in graph[node]:
                dfs(neig, visited)
        
        ans = []
        visited = set()
        dfs(ends[0], visited)
        return ans