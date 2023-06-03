# 1st solution
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