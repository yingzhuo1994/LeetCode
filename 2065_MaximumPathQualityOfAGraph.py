# 1st solution
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append([v, t])
            graph[v].append([u, t])
        
        level = deque([[0, maxTime, 1]])
        ans = 0
        
        @cache
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

# 2nd solution
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        graph = [[] for _ in range(n)]
        for u, v, t in edges:
            graph[u].append([v, t])
            graph[v].append([u, t])
        
        @cache
        def getValue(mask):
            value = 0
            for i in range(n):
                if (mask >> i) & 1:
                    value += values[i]
            return value
        self.ans = 0

        def dfs(node, t, mask):
            if node == 0:
                self.ans = max(self.ans, getValue(mask))
            for neig, cost in graph[node]:
                if cost <= t:
                    dfs(neig, t - cost, mask | (1 << neig))

        dfs(0, maxTime, 1)
        return self.ans
