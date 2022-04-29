# 1st solution, Depth First Search
# O(E) time | O(V) space
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        states = [0] * n
        for i in range(n):
            if states[i] == 0:
                states[i] = 1
                visited = set()
                if not self.dfs(graph, states, visited, i):
                    return False
            else:
                for j in graph[i]:
                    if states[j] == states[i]:
                        return False
                    else:
                        states[j] = -states[i]
        return True
    
    def dfs(self, graph, states, visited, i):
        if i in visited:
            return True
        visited.add(i)
        for j in graph[i]:
            if states[j] == states[i]:
                return False
            states[j] = -states[i]
            if not self.dfs(graph, states, visited, j):
                return False
        return True
