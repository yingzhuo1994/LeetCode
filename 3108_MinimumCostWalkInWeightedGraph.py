# 1st solution
# O(n + m +q) time | O(n + m) space
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, w))

        def dfs(x: int) -> int:
            and_ = -1
            ids[x] = len(cc_and)  # 记录每个点所在连通块的编号
            for y, w in g[x]:
                and_ &= w
                if ids[y] < 0:  # 没有访问过
                    and_ &= dfs(y)
            return and_

        ids = [-1] * n  # 记录每个点所在连通块的编号
        cc_and = []  # 记录每个连通块的边权的 AND
        for i in range(n):
            if ids[i] < 0:
                cc_and.append(dfs(i))

        return [-1 if ids[s] != ids[t] else cc_and[ids[s]]
                for s, t in query]