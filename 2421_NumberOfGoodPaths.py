# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.count = 0

        def dfs(start, node, parent=-1):
            for neigh in graph[node]:
                if neigh == parent:
                    continue
                if vals[neigh] > start:
                    continue
                if vals[neigh] == start:
                    self.count += 1
                dfs(start, neigh, node)
        
        for node in range(n):
            dfs(vals[node], node)
        
        self.count //= 2
        return n + self.count

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        res = n = len(vals)
        parents = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        for v, i, j in edges:
            pi, pj = find(i), find(j)
            ci, cj = count[pi][v], count[pj][v]
            res += ci * cj
            parents[pj] = pi
            count[pi] = Counter({v: ci + cj})

        return res