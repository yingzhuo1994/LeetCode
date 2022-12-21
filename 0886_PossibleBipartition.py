# 1st solution
# O(E + V) time | O(E + V) space
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i, last=0):
            if i in labels:
                return labels[i] * last <= 0
            labels[i] = 1 if last == 0 else -last
            for j in graph[i]:
                if not dfs(j, labels[i]):
                    return False
            return True
    
        labels = {}
        for i in range(1, n + 1):
            if i not in labels:
                if not dfs(i):
                    return False
        return True