# 1st solution, Floyd-Warshall solution
# O（V^3) time | O(V^3) space
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = 1.0
            quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                    quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]

# 2nd solution, disjoint set
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
		# O(|E|)
        disjointSet = DisjointSet()
        for (a, b), v in zip(equations, values):
            disjointSet.add(a) # O(1)
            disjointSet.add(b) # O(1)
            disjointSet.union(a, b, v) # Amortized O(1)

        ans = [] 
		# O(|Q|)
        for a, b in queries:
            ans.append(disjointSet.calc(a, b)) # Amortized O(1)
        
        return ans
     

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.rank = {}

    def add(self, a):
        if a not in self.parents:
            self.parents[a] = (a, 1.0)
            self.rank[a] = 1

    def find(self, x):
        px, v = self.parents[x]
        if x != px:
            # pnx is new part of x
            # pnx/parents[pnx] = vn
            # vn*v is the x/pnx
            pnx, vn = self.find(px) 
            self.parents[x] = pnx, vn*v
        return self.parents[x]
    
    def union(self, a, b, v):
        x, vx = self.find(a)  # a/x = vx
        y, vy = self.find(b) # b/y = vy
        
        if x == y:
            return
        
        # always merging smaller tree into larger one
        # this drastically reduces number of find operations
        if self.rank[x] > self.rank[y]:
            x, y = y, x
            vx, vy = vy, vx
            v = 1.0/v
        
        # v*vy/vx is the value of  x/y
        # x/y = (b/y) * (x/a) * (a/b) = vy * ( 1/vx) *v
        
        self.parents[x] = (y, v * vy / vx) # sub-nodes of x are lazily updated via find later
        self.rank[y] += self.rank[x] # in case of tie
        
    def calc(self, a, b):
        # calculate a/b
        if a not in self.parents or b not in self.parents:
            return -1
            
        x, vx = self.find(a) # vx = a / x
        y, vy = self.find(b) # vy = b / y
        
        if x != y:
            return -1
            
        # a/b = (a/x) * (y/b) * (x/y)
        # x == y
        return vx / vy 