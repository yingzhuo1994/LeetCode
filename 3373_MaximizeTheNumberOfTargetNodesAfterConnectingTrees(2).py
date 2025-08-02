# 1st solution
# O(m + n) time | O(m + n) space 
class Solution:
    def count(self, edges: List[List[int]]) -> Tuple[List[List[int]], List[int]]:
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        cnt = [0, 0]
        def dfs(x: int, fa: int, d: int) -> None:
            cnt[d] += 1
            for y in g[x]:
                if y != fa:
                    dfs(y, x, d ^ 1)
        dfs(0, -1, 0)
        return g, cnt

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        _, cnt2 = self.count(edges2)
        max2 = max(cnt2)

        g, cnt1 = self.count(edges1)
        ans = [max2] * len(g)
        def dfs(x: int, fa: int, d: int) -> None:
            ans[x] += cnt1[d]
            for y in g[x]:
                if y != fa:
                    dfs(y, x, d ^ 1)
        dfs(0, -1, 0)
        return ans