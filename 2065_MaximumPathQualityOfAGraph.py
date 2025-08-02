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

# 3rd solution
# O(n + m * log(m) + 4^k) time | O(n + m + k) space
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], max_time: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))

        # Dijkstra 算法
        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heappush(h, (new_dis, y))

        def dfs(x: int, sum_time: int, sum_value: int) -> None:
            if x == 0:
                nonlocal ans
                ans = max(ans, sum_value)
                # 注意这里没有 return，还可以继续走
            for y, t in g[x]:
                # 相比方法一，这里多了 dis[y]
                if sum_time + t + dis[y] > max_time:
                    continue
                if vis[y]:
                    dfs(y, sum_time + t, sum_value)
                else:
                    vis[y] = True
                    # 每个节点的价值至多算入价值总和中一次
                    dfs(y, sum_time + t, sum_value + values[y])
                    vis[y] = False  # 恢复现场

        ans = 0
        vis = [False] * n
        vis[0] = True
        dfs(0, 0, values[0])
        return ans