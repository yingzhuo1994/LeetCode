# 1st solution, Dijkstra
# O(E+(vk)*log(vk)) time
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        dist = [[float("inf")] * (k+2) for _ in range(n)] 
        dist[src][0] = 0

        SList = SortedList([[0, 0, src]])
        
        for i, j, w in flights: 
            graph[i].append([j, w])
        
        while SList:
            price, visited, city = SList.pop(0)

            if city == dst: return price
            
            if visited <= k:
                for neibh, price_neibh in graph[city]: 
                    candidate = dist[city][visited] + price_neibh
                    if candidate <= dist[neibh][visited + 1]:
                        dist[neibh][visited + 1] = candidate
                        SList.add([price + price_neibh, visited + 1, neibh])
                        
        return -1