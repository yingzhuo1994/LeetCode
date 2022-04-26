# 1st solution, Kruskal's algorithm
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = self.manhattan(points[i], points[j])
                edges.append((dist, i, j))
        
        # sort based on cost (i.e. distance)
        edges.sort()
        
        # using Kruskal's algorithm to find the cost of Minimum Spanning Tree
        res = 0
        ds = DisjointSet(n)
        for cost, u, v in edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                res += cost
        
        return res
    
    def manhattan(self, pointA, pointB):
        x1, y1 = pointA
        x2, y2 = pointB
        return abs(x1 - x2) + abs(y1 - y2)

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
    
    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

# 2nd solution, Prim's algorithm
# O(n^2 * log(n)) time | O(n^2) space
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n, edges = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan(points[i], points[j])
                edges[i].append((dist, j))
                edges[j].append((dist, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, edges[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            dist, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt= 1, cnt + 1
                ans += dist
                for record in edges[j]: 
                    heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans

# 3rd solution, Prim's algorithm (Optimized)
# O(n^2) time | O(n) space
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        mst_cost = 0
        edges_used = 0
        
        # Track nodes which are visited.
        in_mst = [False] * n
        
        min_dist = [float("inf")] * n
        min_dist[0] = 0
        
        while edges_used < n:
            curr_min_edge = float("inf")
            curr_node = -1
            
            # Pick least weight node which is not in MST.
            for node in range(n):
                if not in_mst[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr_node = node
            
            mst_cost += curr_min_edge
            edges_used += 1
            in_mst[curr_node] = True
            
            # Update adjacent nodes of current node.
            for next_node in range(n):
                weight = manhattan(points[curr_node], points[next_node])
                
                if not in_mst[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight
        
        return mst_cost