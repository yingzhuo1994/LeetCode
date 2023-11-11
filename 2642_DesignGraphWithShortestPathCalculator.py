# 1st solution
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for edge in edges:
            self.addEdge(edge)
        
    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append([edge[1], edge[2]])
        
    def shortestPath(self, node1: int, node2: int) -> int:
        dists = [float("inf") for _ in range(self.n)]
        dists[node1] = 0
        minHeap = [[0, node1]]
        while minHeap:
            dist, node = heappop(minHeap)
            if node == node2:
                return dist
            for neig, cost in self.graph[node]:
                newDist = dist + cost
                if dists[neig] > newDist:
                    dists[neig] = newDist
                    heappush(minHeap, [newDist, neig])
        return -1



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)