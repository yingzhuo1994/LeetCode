# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)

        def dfs(node):
            ans = informTime[node]
            cur = 0
            for sub in graph[node]:
                cur = max(cur, dfs(sub))
            return ans + cur

        return dfs(headID)

# 2nd solution, dfs
# O(n) time | O(n) space
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                graph[m].append(i)
        
        level = [[headID, 0]]
        ans = 0
        while level:
            node, t = level.pop()
            newtime = t + informTime[node]
            ans = max(ans, newtime)
            for neig in graph[node]:
                level.append([neig, newtime])
        
        return ans