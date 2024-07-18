# 1st solution
# O(V^2) time | O((V+E) * log(V))
class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])

        dist = [-1 for _ in range(n)]
        dist[0] = 0
        minHeap = [[0, 0]] # time, node

        while minHeap:
            t1, node = heappop(minHeap)
            if t1 > dist[node]:
                continue
            for neig, w in graph[node]:

                t2 = t1 + w
                if t2 < disappear[neig] and (dist[neig] < 0 or t2 < dist[neig]):
                    dist[neig] = t2
                    heappush(minHeap, [t2, neig])
                    
        return dist
