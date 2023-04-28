# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        DS = DisjointSet(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.isSimilar(strs[i], strs[j]):
                    DS.merge(i, j)
        return DS.countParents()
    
    def isSimilar(self, s, t):
        if Counter(s) != Counter(t):
            return False
        count = 0
        for a, b in zip(s, t):
            if a != b:
                count += 1
        return count <= 2

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1] * n
    
    def merge(self, a, b):
        pa, pb = self.getParent(a), self.getParent(b)
        if pa == pb:
            return None
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parents[pb] = pa
        self.size[pa] += self.size[pb]

    def getParent(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]
    
    def countParents(self):
        pSet = set()
        for x in self.parents:
            p = self.getParent(x)
            pSet.add(p)
        return len(pSet)