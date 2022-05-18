# 1st solution
# O(E + V) time | O(E + V) space
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(rank, curr, prev):
            ranks[curr], result = rank, []
            for neighbor in edges[curr]:
                if neighbor == prev: continue
                if not ranks[neighbor]:
                    result += dfs(rank + 1, neighbor, curr)
                ranks[curr] = min(ranks[curr], ranks[neighbor])
                if ranks[neighbor] >= rank + 1:
                    result.append([curr, neighbor])
            return result

        ranks, edges = [0] * n, [[] for _ in range(n)]
        for u, v in connections:
            edges[u].append(v)
            edges[v].append(u)

        return dfs(1, 0, -1)