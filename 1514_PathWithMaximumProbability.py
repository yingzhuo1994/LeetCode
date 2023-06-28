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
