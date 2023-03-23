# 1st soluiton, disojint set
# O(n) time | O(n) space
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        DS = DisjointSet(n)
        for a, b in connections:
            DS.merge(a, b)
        
        return DS.getAnswer()
        

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.extra = 0
    
    def merge(self, a, b):
        pa = self.getParent(a)
        pb = self.getParent(b)
        if pa == pb:
            self.extra += 1
            return
        self.parents[pb] = pa
    
    def getParent(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.getParent(self.parents[x])
        return self.parents[x]
    
    def countUniqParents(self):
        parentSet = set()
        for i in range(len(self.parents)):
            p = self.getParent(i)
            parentSet.add(p)
        return len(parentSet)
    
    def getAnswer(self):
        ans = self.countUniqParents() - 1
        if ans <= self.extra:
            return ans
        else:
            return -1
