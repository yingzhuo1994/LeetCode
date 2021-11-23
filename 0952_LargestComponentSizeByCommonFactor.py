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

# 2nd solution
class DSU:
    def __init__(self, N):
        self.p = list(range(N))
	# keep finding til we reach the parent
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
        
	# point y to x (x as parent)
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
	# Function to generate primes set for number n
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])
        
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        UF = DSU(n)
        primes = collections.defaultdict(list)
        # calculate primes set for all elements in nums
        for i, num in enumerate(nums):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)
		# union disjoint set based on same primes
        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])
		# Count the apperance of parents, return the maxium one
		# Since all connected nodes will point to same parent
        return max(collections.Counter([UF.find(i) for i in range(n)]).values())