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

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0 for _ in range(n)]
        count = 0
        for i in range(n):
            if visited[i] == 0:
                self.dfs(isConnected, visited, i)
                count += 1
        return count
    
    def dfs(self, matrix, visited, i):
        visited[i] = 1
        for j in range(len(matrix)):
            if matrix[i][j] == 1 and visited[j] == 0:
                self.dfs(matrix, visited, j)

# 3rd solution
# O(n^2) time | O(n) space
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        n = len(isConnected)
        def dfs(node):
            if isConnected[node][node] == -1:
                return -1
            count = 1
            isConnected[node][node] = -1
            for neig in range(n):
                if isConnected[node][neig]:
                    count += max(dfs(neig), 0)
            return count
        
        for i in range(n):
            if dfs(i) > 0:
                ans += 1
        return ans