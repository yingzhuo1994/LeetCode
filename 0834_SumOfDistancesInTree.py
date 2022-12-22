# 1st solution, TLE
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(idx, i):
            for j in graph[i]:
                if dp[idx][j] != -1:
                    continue
                dp[idx][j] = dp[idx][i] + 1
                dp[j][idx] = dp[idx][i] + 1
                dfs(idx, j)


        for i in range(n):
            dfs(i, i)
        
        return [sum(row) for row in dp]