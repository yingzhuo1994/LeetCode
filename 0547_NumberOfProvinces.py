# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        DS = DisjointSet()
        n = len(isConnected)
        for i in range(n):
            DS.add(i)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    DS.merge(i, j)
        
        return DS.countSet()

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.size = {}
    
    def add(self, node):
        if node not in self.parents:
            self.parents[node] = node
            self.size[node] = 1
    
    def merge(self, node1, node2):
        p1 = self.getParent(node1)
        p2 = self.getParent(node2)
        if p1 == p2:
            return None
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
            node1, node2 = node2, node1
        self.parents[p2] = p1
        self.size[p1] += self.size[p2]

    def getParent(self, node):
        if self.parents[node] != node:
            self.parents[node] = self.getParent(self.parents[node])
        return self.parents[node]
    
    def countSet(self):
        ans = set()
        for node in self.parents:
            p = self.getParent(node)
            ans.add(p)
        return len(ans)