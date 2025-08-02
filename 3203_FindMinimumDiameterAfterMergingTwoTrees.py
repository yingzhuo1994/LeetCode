# 1st solution
# O(m + n) time | O(m + n) space
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        p1, d1 = self.help(edges1)
        p2, d2 = self.help(edges2)
        return max(d1, d2, p1 + p2) - 1
    
    def help(self, edges):
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        return self.bfs(graph)
    
    
    def bfs(self, graph):
        n = len(graph)
        values = [[0, 0, 1] for _ in range(n)]
        degrees = [len(lst) for lst in graph]
        leaves = [node for node in range(n) if degrees[node] == 1]
        while leaves:
            newLeaves = []
            for leave in leaves:
                for neig in graph[leave]:
                    if degrees[neig] == 0:
                        continue
                    if values[leave][0] + 1 > values[neig][0]:
                        values[neig][0], values[neig][1] = values[leave][0] + 1, values[neig][0]
                    elif values[leave][0] + 1 > values[neig][1]:
                        values[neig][1] = values[leave][0] + 1
                    values[neig][2] = max(values[leave][2], values[neig][0] + values[neig][1] + 1)
                    degrees[neig] -= 1
                    if degrees[neig] == 1:
                        newLeaves.append(neig)
                degrees[leave] = 0
            leaves = newLeaves
        p = max([values[node][0] for node in range(n)])
        d = max([values[node][2] for node in range(n)])
        return p + 1, d