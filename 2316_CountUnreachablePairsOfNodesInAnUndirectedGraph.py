# 1st solution, dfs, TLE
# O(n) time | O(n) space
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0 for _ in range(n)]

        def dfs(node):
            visited[node] = 1
            count = 1
            for neig in graph[node]:
                if visited[neig]:
                    continue
                count += dfs(neig)
            return count

        lst = []
        for i in range(n):
            if visited[i]:
                continue
            count = dfs(i)
            lst.append(count)
        
        ans = 0
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                ans += lst[i] * lst[j]
        
        return ans