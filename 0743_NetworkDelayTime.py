# 1st solution
# O(E + VE) time | O(V + E) space
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            edges[u].append([v, w])

        dists = {i: float("inf") for i in range(1, n + 1)}
        dists[k] = 0

        visited = set()
        while True:
            dist = float("inf")
            candidate = None
            for i in range(1, n + 1):
                if i not in visited and dists[i] < dist:
                    dist = dists[i]
                    candidate = i
            
            if candidate == None:
                break

            visited.add(candidate)
            for v, w in edges[candidate]:
                newDist = dist + w
                if newDist < dists[v]:
                    dists[v] = newDist
        
        ans = max(dists.values())
        return ans if ans != float("inf") else -1