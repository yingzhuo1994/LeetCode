# 1st solution
# O(mn) time | O(m + n) space
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)

        time = [0] * n  # 充当 vis 数组的作用（避免在 BFS 内部重复创建 vis 数组）
        clock = 0
        def bfs(start: int) -> int:  # 返回从 start 出发的最大深度
            depth = 0
            nonlocal clock
            clock += 1
            time[start] = clock
            q = [start]
            while q:
                tmp = q
                q = []
                for x in tmp:
                    for y in graph[x]:
                        if time[y] != clock:  # 没有在同一次 BFS 中访问过
                            time[y] = clock
                            q.append(y)
                depth += 1
            return depth

        color = [0] * n
        def is_bipartite(x: int, c: int) -> bool:  # 二分图判定，原理见视频讲解
            nodes.append(x)
            color[x] = c
            for y in graph[x]:
                if color[y] == c or color[y] == 0 and not is_bipartite(y, -c):
                    return False
            return True

        ans = 0
        for i, c in enumerate(color):
            if c: continue
            nodes = []
            if not is_bipartite(i, 1): return -1  # 如果不是二分图（有奇环），则无法分组
            # 否则一定可以分组
            ans += max(bfs(x) for x in nodes)  # 枚举连通块的每个点，作为起点 BFS，求最大深度
        return ans