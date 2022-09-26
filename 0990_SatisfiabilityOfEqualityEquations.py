class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ds = DisjointSet()
        unequals = []
        for equation in equations:
            a, b = equation[0], equation[3]
            ds.add(a)
            ds.add(b)
            if equation[1] == "=":
                ds.union(a, b)
            else:
                unequals.append([a, b])
        
        for a, b in unequals:
            if ds.getParent(a) == ds.getParent(b):
                return False
        return True

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.size = {}
    
    def add(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.size[x] = 1
    
    def union(self, a, b):
        pa = self.getParent(a)
        pb = self.getParent(b)
        if pa == pb:
            return
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
            a, b = b, a
        self.parents[pb] = pa
        self.size[pa] += self.size[pb]
    
    def getParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]