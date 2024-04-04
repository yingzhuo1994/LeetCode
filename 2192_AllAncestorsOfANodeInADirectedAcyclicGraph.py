# 1st solution
# O(VE + V^2 * log(V)) time | O(V^2) space
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inCounts = [0 for _ in range(n)]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[b].append(a)
            inCounts[a] += 1
        
        ans = [[] for _ in range(n)]
        
        @cache
        def getChildren(node):
            if len(graph[node]) == 0:
                return []

            for neig in graph[node]:
                ans[node].extend([neig] + getChildren(neig))
            ans[node] = sorted(list(set(ans[node])))
            return ans[node]
        
        sources = [node for node in range(n) if inCounts[node] == 0]
        for node in sources:
            getChildren(node)
        return ans
        

# 2nd solution
# O(n(n + m)) time | O(n + m) space
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        for x, y in edges:
            graph[y].append(x)  # 反向建图

        def dfs(x: int) -> None:
            vis[x] = True  # 避免重复访问
            for y in graph[x]:
                if not vis[y]:
                    dfs(y)  # 只递归没有访问过的点

        ans = [None] * n
        for node in range(n):
            vis = [False] * n
            dfs(node)  # 从 node 开始 DFS
            vis[node] = False  # ans[i] 不含 i
            ans[node] = [j for j, b in enumerate(vis) if b]
        return ans