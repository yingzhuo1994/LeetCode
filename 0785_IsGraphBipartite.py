# 1st solution, Depth First Search
# O(E+V) time | O(V) space
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        states = [0] * n
        for i in range(n):
            if states[i] == 0:
                states[i] = 1
                if not self.dfs(graph, states, i):
                    return False
        return True
    
    def dfs(self, graph, states, i):
        for j in graph[i]:
            if states[j] != 0:
                if states[j] == states[i]:
                    return False
            else:
                states[j] = -states[i]
                if not self.dfs(graph, states, j):
                    return False
        return True
