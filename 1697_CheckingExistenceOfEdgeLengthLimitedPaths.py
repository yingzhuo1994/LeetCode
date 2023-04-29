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