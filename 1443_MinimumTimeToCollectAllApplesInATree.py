# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(idx, parent=-1):
            count = 0
            isValid = False
            for i in graph[idx]:
                if i != parent:
                    isChildValid, childCount = dfs(i, idx)
                    if isChildValid:
                        isValid = True
                        count += childCount + 2
            if hasApple[idx]:
                isValid = True
            return isValid, count
        
        _, ans = dfs(0)
        return ans