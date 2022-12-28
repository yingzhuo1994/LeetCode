# 1st solution, TLE
# O(n^2) time | O(n^2) space
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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        def dfs(node, parent, depth):
            ans = 1
            for neib in graph[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        
        def dfs2(node, parent, w):
            ans[node] = w
            for neib in graph[node]:
                if neib != parent:
                    dfs2(neib, node, w + n - 2*weights[neib])
        
        weights, depths, ans = [0]*n, [0]*n, [0]*n
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        
        return ans

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        def dfs_depth(node, parent, depth):
            depths[node] = depth
            for neib in graph[node]:
                if neib != parent:
                    dfs_depth(neib, node, depth + 1)

        def dfs_weight(node, parent):
            ans = 1
            for neib in graph[node]:
                if neib != parent:
                    ans += dfs_weight(neib, node)
            weights[node] = ans
            return ans
        
        def dfs_dist(node, parent, w):
            ans[node] = w
            for neib in graph[node]:
                if neib != parent:
                    dfs_dist(neib, node, w + n - 2*weights[neib])
        
        weights, depths, ans = [0]*n, [0]*n, [0]*n
        dfs_depth(0, -1, 0)
        dfs_weight(0, -1)
        dfs_dist(0, -1, sum(depths))
        
        return ans