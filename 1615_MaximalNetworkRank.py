# 1st solution
# O(n^2) time | O(n + len(roads)) space
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
    
# 2nd solution
# O(n^2) time | O(n + len(roads)) space
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        road_set = set(tuple(road) for road in roads)
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if (i, j) in road_set or (j, i) in road_set:
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank