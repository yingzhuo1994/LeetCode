# 1st solution, TLE
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append([v, t])
            graph[v].append([u, t])
        
        level = deque([[0, maxTime, 1]])
        ans = 0

        def getValue(mask):
            value = 0
            for i in range(n):
                if (mask >> i) & 1:
                    value += values[i]
            return value
        while level:
            node, t, mask = level.popleft()
            if node == 0:
                ans = max(ans, getValue(mask))
            for neig, cost in graph[node]:
                if cost <= t:
                    level.append([neig, t - cost, mask | (1 << neig)])
        return ans