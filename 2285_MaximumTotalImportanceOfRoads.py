# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        degree = [[i, len(graph[i])] for i in range(n)]
        degree.sort(key=lambda v: v[1])
        weights = [0 for _ in range(n)]
        i = 1
        for idx, _ in degree:
            weights[idx] = i
            i += 1
        ans = 0
        for a, b in roads:
            ans += weights[a] + weights[b]
        return ans