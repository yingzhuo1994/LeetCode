# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append([b, p])
            graph[b].append([a, p])
        
        dp = [0] * n
        dp[start] = 1.0
        visited = [False] * n
        for _ in range(n):
            k = -1
            p = 0
            for node in range(n):
                if not visited[node] and dp[node] > p:
                    p = dp[node]
                    k = node
            if k == -1:
                break
            visited[k] = True
            for neig, nextP in graph[k]:
                dp[neig] = max(dp[neig], p * nextP)
        
        return dp[end]

# 2nd solution, Bellman Ford
# O(V * E) time | O(V + E) space
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append([b, p])
            graph[b].append([a, p])
        
        dp = [0] * n
        dp[start] = 1.0
        stack = [start]
        while stack:
            newStack = []
            for node in stack:
                for neig, edgeP in graph[node]:
                    newP = dp[node] * edgeP
                    if newP > dp[neig]:
                        dp[neig] = newP
                        newStack.append(neig)
            
            stack = newStack

        return dp[end]

# 3rd solution, Dijkstra
# O((V * E) * log(E)) time | O(V + E) space
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            p = succProb[i]
            graph[a].append([b, p])
            graph[b].append([a, p])
        dp = [0] * n
        dp[start] = 1.0
        heap = [(-dp[start], start)]
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neig, p in graph[cur]:
                newP = -prob * p
                if newP > dp[neig]:
                    dp[neig] = newP
                    heapq.heappush(heap, (-dp[neig], neig))
        
        return 0.0