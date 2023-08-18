# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                neig1 = set(graph[i])
                neig2 = set(graph[j])
                if j in neig1:
                    neig1.remove(j)
                ans = max(ans, len(neig1) + len(neig2))
        
        return ans