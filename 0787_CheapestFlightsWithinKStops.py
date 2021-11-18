# 1st solution, Dijkstra
# O(E+(vk)*log(vk)) time
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, k + 1)]
        visited = [0] * n
        while pq:
            w, city, stops = heapq.heappop(pq)
            if city == dst:
                return w
            if visited[city] >= stops:
                continue
            visited[city] = stops
            for neibh, dw in graph[city].items():
                heapq.heappush(pq, (w + dw, neibh, stops - 1))
        return -1

# 2nd solution
# Bellman-Ford Algorithm
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf") for i in range(n)]
        dist[src] = 0
        
        # Run only K+1 times since we want shortest distance in K hops
        for i in range(k + 1):
            tmp = dist[:]
            for flight in flights:
                if dist[flight[0]] != float("inf"):
                    tmp[flight[1]] = min(tmp[flight[1]], dist[flight[0]] + flight[2])
            dist = tmp

        return -1 if dist[dst] == float("inf") else dist[dst]