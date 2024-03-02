# 1st solution
# O(n) time | O(n) space
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node, prev):
            count = 1
            for neig in graph[node]:
                if neig == prev or neig in restricted:
                    continue
                count += dfs(neig, node)
            return count
        restricted = set(restricted)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        return dfs(0, None)
