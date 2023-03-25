# 1st solution, dfs
# O(n) time | O(n) space
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [0 for _ in range(n)]

        def dfs(node):
            visited[node] = 1
            count = 1
            for neig in graph[node]:
                if visited[neig]:
                    continue
                count += dfs(neig)
            return count

        values = []
        for i in range(n):
            if visited[i]:
                continue
            count = dfs(i)
            values.append(count)
        
        ans = 0
        count = 0
        for value in values:
            count += value
            ans += value * (n - count)
        return ans

# 2nd solution, Disjoint Set
# O(n) time | O(n) space
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        DS = DisjointSet(n)
        for a, b in edges:
            DS.merge(a, b)
        
        countDic = DS.getCountDic()
        ans = 0
        values = list(countDic.values())
        count = 0
        for value in values:
            count += value
            ans += value * (n - count)
        return ans

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def merge(self, a, b):
        pa = self.getParent(a)
        pb = self.getParent(b)
        if pa == pb:
            return
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        
        self.parents[pb] = pa
        self.size[pa] += self.size[pb]
    
    def getParent(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.getParent(self.parents[a])
        return self.parents[a]
    
    def getCountDic(self):
        dic = {}
        for node in range(len(self.parents)):
            parent = self.getParent(node)
            if parent not in dic:
                dic[parent] = self.size[parent]
        return dic