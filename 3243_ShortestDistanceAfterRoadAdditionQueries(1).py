# 1st solution
# O(kn) time | O(n + k) space
# where k = len(queries)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph_rev = [[] for _ in range(n)]
        for i in range(n - 1):
            graph_rev[i + 1].append(i)
        dp = [n - 1 - i for i in range(n)]
        def dfs(start):
            for neig in graph_rev[start]:
                if dp[neig] > dp[start] + 1:
                    dp[neig] = dp[start] + 1
                    dfs(neig)
        ans = []
        for u, v in queries:
            if dp[0] == 1:
                ans.append(1)
                continue
            graph_rev[v].append(u)
            dp[u] = min(dp[u], dp[v] + 1)
            dfs(u)
            ans.append(dp[0])
        return ans


# 2nd solution
# O(k(n + k)) time | O(n + k) space
# where k = len(queries)
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        neighbors = [[i + 1] for i in range(n)]
        neighbors[-1] = []
        res = []
        for (u, v) in queries:
            neighbors[u].append(v)
            res.append(self.bfs(n, neighbors))
        return res

    def bfs(self, n: int, neighbors: List[List[int]]) -> int:
        dist = [-1 for _ in range(n)]
        dist[0] = 0
        q = deque([0])
        while len(q) > 0:
            x = q.popleft()
            for y in neighbors[x]:
                if dist[y] >= 0:
                    continue
                q.append(y)
                dist[y] = dist[x] + 1
        return dist[n - 1]