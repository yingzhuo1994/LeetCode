# 1st solution, TLE
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        disjointSet = DisjointSet()
        for num in nums:
            disjointSet.add(num)
        
        n = len(nums)
        for i in range(n):
            for j in range(i):
                disjointSet.union(nums[i], nums[j])
        
        return disjointSet.getMaxSize()

class DisjointSet:
    def __init__(self):
        self.parents = {}
        self.size = {}
        self.maxSizeElem = None
        self.maxSize = 0

    def add(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.size[x] = 1
            if self.maxSize == 0:
                self.maxSize = 1
                self.maxSizeElem = x

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        if self.gcd(x, y) <= 1:
            return 
        px, py = self.find(x), self.find(y)
        if px == py:
            return 
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parents[py] = px
        self.size[px] += self.size[py]
        if self.size[px] > self.maxSize:
            self.maxSize = self.size[px]
            self.maxSizeElem = px
    
    def gcd(self, a, b):
        while a % b > 0:
            a, b = b, a % b
        return b
    
    def getMaxSize(self):
        return self.maxSize