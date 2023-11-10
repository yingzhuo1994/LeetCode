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
        def dfs(node, prev):
            ans.append(node)
            for neig in graph[node]:
                if neig == prev:
                    continue
                dfs(neig, node)
        
        ans = []
        dfs(ends[0], None)
        return ans