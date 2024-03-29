# 1st solution, TLE
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        def find_path(source, target, prev=-1):
            if source == target:
                return [0]
            for neig, weight in graph[source]:
                if neig == prev:
                    continue
                if neig == target:
                    return [weight]
                lst = find_path(neig, target, source)
                if len(lst) > 0:
                    return [weight] + lst
            
            return []
        
        def get_answer(u, v):
            path = find_path(u, v)
            if len(path) > 0:
                count = Counter(path)
                max_freq = max(count.values())
                return len(path) - max_freq
            
            return -1
        
        return [get_answer(u, v) for u, v in queries]

# 2nd solution
# O((n + q) * U * log(n)) time | O(n * U * log(n)) space
# where q = len(queries) and U = unique number of edge weights
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w - 1))
            g[y].append((x, w - 1))

        m = n.bit_length()
        pa = [[-1] * m for _ in range(n)]
        cnt = [[[0] * 26 for _ in range(m)] for _ in range(n)]
        depth = [0] * n
        def dfs(x: int, fa: int) -> None:
            pa[x][0] = fa
            for y, w in g[x]:
                if y != fa:
                    cnt[y][0][w] = 1
                    depth[y] = depth[x] + 1
                    dfs(y, x)
        dfs(0, -1)

        # 倍增模板
        for i in range(m - 1):
            for x in range(n):
                p = pa[x][i]
                if p != -1:
                    pp = pa[p][i]
                    pa[x][i + 1] = pp
                    for j, (c1, c2) in enumerate(zip(cnt[x][i], cnt[p][i])):
                        cnt[x][i + 1][j] = c1 + c2

        ans = []
        for x, y in queries:
            path_len = depth[x] + depth[y]  # 最后减去 depth[lca] * 2
            cw = [0] * 26
            if depth[x] > depth[y]:
                x, y = y, x

            # 使 y 和 x 在同一深度
            k = depth[y] - depth[x]
            for i in range(k.bit_length()):
                if (k >> i) & 1:  # k 二进制从低到高第 i 位是 1
                    p = pa[y][i]
                    for j, c in enumerate(cnt[y][i]):
                        cw[j] += c
                    y = p

            if y != x:
                for i in range(m - 1, -1, -1):
                    px, py = pa[x][i], pa[y][i]
                    if px != py:
                        for j, (c1, c2) in enumerate(zip(cnt[x][i], cnt[y][i])):
                            cw[j] += c1 + c2
                        x, y = px, py  # 同时上跳 2^i 步
                for j, (c1, c2) in enumerate(zip(cnt[x][0], cnt[y][0])):
                    cw[j] += c1 + c2
                x = pa[x][0]

            lca = x
            path_len -= depth[lca] * 2
            ans.append(path_len - max(cw))
        return ans