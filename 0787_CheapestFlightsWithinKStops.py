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