# 1st solution, TLE
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        numSet = set(nums)
        if 1 in numSet:
            return False

        numToPrime = {}
        
        n = max(nums)
        primes = [True for _ in range(n + 1)]
        primes[0] = False
        primes[1] = False
        primeDict = {}
        primeList = []
        for i in range(2, n + 1):
            if primes[i]:
                primes[i+i::i] = [False] * len(primes[i+i::i])
                primeList.append(i)
                primeDict[i] = set()
        
        def getPrimes(num):
            ans = []
            for prime in primeList:
                if num % prime == 0:
                    ans.append(prime)
                if prime > num:
                    break
            return ans
        
        for num in numSet:
            lst = getPrimes(num)
            product = 1
            for v in lst:
                product *= v
            if product not in numToPrime:
                numToPrime[product] = lst
                for prime in lst:
                    primeDict[prime].add(product)
        
        m = max(numToPrime)
        visited = set([m])
        level = set([m])
        while level:
            newLevel = set()
            for num in level:
                for prime in numToPrime[num]:
                    new = primeDict[prime].difference(visited)
                    newLevel |= new
                    visited |= new
            level = newLevel
        
        return len(visited) == len(numToPrime)

# 2nd solution
# O(n^2 * log(m)) time | O(m) space
# where n = len(nums), m = max(nums)
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # corner case 1
        if len(nums) == 1:
            return True
        
        # corner case 2
        if 1 in nums: 
            return False

        nums = sorted(set(nums), reverse=True)    # <-- sort (big to little) and  
        if (n:=len(nums))==1:
            return True          #     deal with another edge case

        for i in range(n-1):                        # <-- nums[i] >= nums[j]
            for j in range(i+1,n):
                if gcd(nums[i], nums[j])-1:          # <-- i,j traversal exists; 
                    nums[j] *= nums[i]              # <-- if an i,k traversal exists   
                    break                           #     (for some index k), then now 
                                                    #     a j,k traversal exists
            else:
                return False                      # <-- no match means no traversal 

        return True 


# 3rd solution
class Solution:
    def dfs(self, index, visitedIndex, visitedPrime):
        if visitedIndex[index]:
            return
        visitedIndex[index] = True

        for prime in self.index2prime[index]:
            if visitedPrime.get(prime, False):
                continue
            visitedPrime[prime] = True
            for index1 in self.prime2index[prime]:
                if visitedIndex[index1]:
                    continue
                self.dfs(index1, visitedIndex, visitedPrime)

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # corner case 1
        if len(nums) == 1:
            return True
        
        # corner case 2
        if 1 in nums: 
            return False
        
        self.prime2index = {}
        self.index2prime = {}
        for i, num in enumerate(nums):
            temp = num
            for j in range(2, int(num ** 0.5) + 1):
                if temp % j == 0:
                    self.prime2index.setdefault(j, []).append(i)
                    self.index2prime.setdefault(i, []).append(j)
                    while temp % j == 0:
                        temp //= j
            if temp > 1:
                self.prime2index.setdefault(temp, []).append(i)
                self.index2prime.setdefault(i, []).append(temp)

        visitedIndex = [False] * len(nums)
        visitedPrime = {}
        self.dfs(0, visitedIndex, visitedPrime)

        return all(visitedIndex)
