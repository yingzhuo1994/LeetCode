# 1st solution, TLE
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = {}
        for x, y, t in meetings:
            if t not in dic:
                dic[t] = DisjointSet()
            dic[t].add(x)
            dic[t].add(y)
            dic[t].merge(x, y)
        
        times = sorted(list(dic.keys()))
        ans = set([0, firstPerson])
        for t in times:
            persons = dic[t].getPerson()
            for p in persons:
                parent = dic[t].getParent(p)
                if p in ans or parent in ans:
                    ans |= dic[t].size[parent]
            
        return list(ans)
    
class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.size = {}
    
    def add(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.size[x] = set([x])
    
    def merge(self, a, b):
        pa, pb = self.getParent(a), self.getParent(b)
        if pa == pb:
            return
        if len(self.size[pa]) < len(self.size[pb]):
            a, b = b, a
            pa, pb = pb, pa
        self.parents[pb] = pa
        self.size[pa] |= self.size[pb]
    
    def getParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]
    
    def hasSameParent(self, a, b):
        return self.getParent(a) == self.getParent(b)
    
    def getPerson(self):
        return self.parents.keys()


# 2nd solution
# O(m) time | O(m) space
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dic = {}
        for x, y, t in meetings:
            if t not in dic:
                dic[t] = {}
            if x not in dic[t]:
                dic[t][x] = []
            if y not in dic[t]:
                dic[t][y] = []
            dic[t][x].append(y)
            dic[t][y].append(x)
        
        def dfs(node, visited, graph):
            if node in visited:
                return set()
            s = set()
            s.add(node)
            visited.add(node)
            for neig in graph[node]:
                s |= dfs(neig, visited, graph)
            return s

        times = sorted(list(dic.keys()))
        ans = set([0, firstPerson])
        for t in times:
            graph = dic[t]
            visited = set()
            for node in graph:
                if node in visited:
                    continue
                if node in ans:
                    neigs = dfs(node, visited, graph)
                    ans |= neigs
            
        return list(ans)