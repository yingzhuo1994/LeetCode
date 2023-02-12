# 1st solution
# O(n) time | O(n) space
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        depths = [0 for _ in range(n)]
        children = [0 for _ in range(n)]
        def dfs(node, depth, parent=-1):
            depths[node] = depth
            count = 1
            for neig in graph[node]:
                if neig == parent:
                    continue
                count += dfs(neig, depth + 1, node)
            children[node] = count
            return count
        
        dfs(0, 0)
        ans = 0
        for i in range(1, n):
            k, r = divmod(children[i], seats)
            if r > 0:
                k += 1
            ans += k

        return ans