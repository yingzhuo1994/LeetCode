# 1st solution
# O(n^2 + m^2) time | O(n + m) space
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1
        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]
        for a, b in edges1:
            graph1[a].append(b)
            graph1[b].append(a)
        
        for a, b in edges2:
            graph2[a].append(b)
            graph2[b].append(a)
        
        def dfs1(graph, node, last, dist):
            cnt = 0
            if dist == 0:
                return 1
            for neig in graph[node]:
                if neig == last:
                    continue
                cnt += dfs1(graph, neig, node, dist - 1)
            return cnt + 1
        
        @cache
        def dfs2(t):
            if t < 0:
                return 0
            return max([dfs1(graph2, i, None, t) for i in range(m)])

        ans = []
        for i in range(n):
            cnt = dfs1(graph1, i, None, k)
            cnt += dfs2(k - 1)
            ans.append(cnt)
        
        return ans