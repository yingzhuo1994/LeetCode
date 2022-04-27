# 1st solution
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        disjointSet = DisjointSet()
        for a, b in pairs:
            disjointSet.add(a, s[a])
            disjointSet.add(b, s[b])
            disjointSet.union(a, b)
        
        stack = list(s)
        for i in range(len(stack)):
            if i not in disjointSet.parent:
                continue
            candidate = ""
            dataSet = disjointSet.getDataSet(i)

            for k in string.ascii_lowercase:
                if dataSet[k] > 0:
                    candidate = k
                    break
                    
            stack[i] = candidate
            dataSet[candidate] -= 1

        return "".join(stack)

class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.dataSet = {}
    
    def add(self, a, ch):
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 1
            self.dataSet[a] = {ch : 0 for ch in string.ascii_lowercase}
            self.dataSet[a][ch] = 1
    
    # make a and b part of the same component
    # union by rank optimization
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        if pa == pb: return
        if self.rank[pa] > self.rank[pb]:
            self.parent[pb] = pa
            self.rank[pa] += self.rank[pb]
            for k, v in self.dataSet[pb].items():
                self.dataSet[pa][k] += v
        else:
            self.parent[pa] = pb
            self.rank[pb] += self.rank[pa]
            for k, v in self.dataSet[pa].items():
                self.dataSet[pb][k] += v

    # find the representative of the 
    # path compression optimization
    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def getDataSet(self, a):
        parent = self.find(a)
        return self.dataSet[parent]