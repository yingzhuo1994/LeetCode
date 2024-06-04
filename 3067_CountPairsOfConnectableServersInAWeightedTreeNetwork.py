# 1st solution
class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])
        
        def dfs(node, prev, dist):
            count = 0
            if dist % signalSpeed == 0:
                count += 1
            for neig, w in graph[node]:
                if neig == prev:
                    continue
                count += dfs(neig, node, dist + w)

            return count
        
        ans = []
        for node in range(n):
            lst = []
            for neig, w in graph[node]:
                lst.append(dfs(neig, node, w))
            count = 0
            curSum = 0
            for val in lst:
                count += curSum * val
                curSum += val
            ans.append(count)
        
        return ans