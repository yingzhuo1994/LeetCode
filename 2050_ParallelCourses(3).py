# 1st solution, TLE
# O(n) time | O(n) space
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = [[] for _ in range(n + 1)]
        inCount = [0 for _ in range(n + 1)]
        outCount = [0 for _ in range(n + 1)]

        for a, b in relations:
            graph[a].append(b)
            inCount[b] += 1
            outCount[a] += 1
        
        self.ans = 0
        def dfs(node, t):
            if outCount[node] == 0:
                self.ans = max(self.ans, t + time[node - 1])
                return
            for neig in graph[node]:
                dfs(neig, t + time[node - 1])
        
        for node in range(1, n + 1):
            if inCount[node] == 0:
                dfs(node, 0)
        
        return self.ans