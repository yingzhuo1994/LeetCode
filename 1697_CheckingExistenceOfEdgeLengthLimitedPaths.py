# 1st solution, TLE
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(n)]
        dic = {}
        for src, dst, cost in edgeList:
            if src > dst:
                src, dst = dst, src
            key = (src, dst)
            if key in dic:
                dic[key] = min(dic[key], cost)
            else:
                dic[key] = cost
        
        for src, dst in dic:
            cost = dic[(src, dst)]
            graph[src].append([dst, cost])
            graph[dst].append([src, cost])
        
        def dfs(node, target, limit, visiting=set()):
            if node == target:
                return True
            visiting.add(node)
            for dst, cost in graph[node]:
                if dst in visiting:
                    continue
                if cost >= limit:
                    continue
                if dfs(dst, target, limit, visiting):
                    return True
            return False
        
        ans = [False] * len(queries)
        for i in range(len(queries)):
            src, dst, limit = queries[i]
            ans[i] = dfs(src, dst, limit, set())
        return ans

# 2nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        queries = sorted((w, p, q, i) for i, (p, q, w) in enumerate(queries))
        edgeList = sorted((w, u, v) for u, v, w in edgeList)
        
        uf = UnionFind(n)
        
        ans = [None] * len(queries)
        ii = 0
        for w, p, q, i in queries: 
            while ii < len(edgeList) and edgeList[ii][0] < w: 
                _, u, v = edgeList[ii]
                uf.union(u, v)
                ii += 1
            ans[i] = uf.find(p) == uf.find(q)
        return ans

class UnionFind:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.rank = [1] * N

    def find(self, p: int) -> int:
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p: int, q: int) -> bool:
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False 
        if self.rank[prt] > self.rank[qrt]: 
            prt, qrt = qrt, prt 
        self.parent[prt] = qrt 
        self.rank[qrt] += self.rank[prt] 
        return True 