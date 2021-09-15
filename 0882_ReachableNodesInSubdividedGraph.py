class Solution:
    # 1st solution, Dijkstra's algorithm
    # O(ElogN) time | O(E) space
    # where E is the length of edges, N is the number of nodes
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w

        pq = [(0, 0)]
        dist = {0: 0}
        used = {}
        ans = 0

        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]: continue
            # Each node is only visited once.  We've reached
            # a node in our original graph.
            ans += 1

            for nei, weight in graph[node].items():
                # maxMoves - d is how much further we can walk from this node;
                # weight is how many new nodes there are on this edge.
                # v is the maximum utilization of this edge.
                v = min(weight, maxMoves - d)
                used[node, nei] = v

                # d2 is the total distance to reach 'nei' (neighbor) node
                # in the original graph.
                d2 = d + weight + 1
                if d2 < dist.get(nei, maxMoves + 1):
                    heapq.heappush(pq, (d2, nei))
                    dist[nei] = d2

        # At the end, each edge (u, v, w) can be used with a maximum
        # of w new nodes: a max of used[u, v] nodes from one side,
        # and used[v, u] nodes from the other.
        for u, v, w in edges:
            ans += min(w, used.get((u, v), 0) + used.get((v, u), 0))

        return ans

    # 2nd solution
    # O(ElogN) time | O(E) space
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        G = collections.defaultdict(set)
        dist = [float('inf')] * n
        dist[0] = 0
        
        for i, j, w in edges:
            G[i].add((j, w + 1))
            G[j].add((i, w + 1))
            
        heap = [(0, 0)]

        while heap:
            min_dist, idx = heappop(heap)
            for neibh, weight in G[idx]:
                cand = min_dist + weight
                if cand < dist[neibh]:
                    dist[neibh] = cand
                    heappush(heap, (cand, neibh)) 
                    
        ans = sum(dist[i] <= maxMoves for i in range(n))
 
        for i, j, w in edges:
            w1, w2 = maxMoves - dist[i], maxMoves - dist[j]
            ans += (max(0, w1) + max(0, w2))
            if w1 >= 0 and w2 >= 0: ans -= max(w1 + w2 - w, 0)
                
        return ans