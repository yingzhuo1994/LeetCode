# 1st solution, TLE
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        numSet = set(nums)
        if len(numSet) == 1:
            if nums[0] == 1 and len(nums) > 1:
                return False
            return True

        numToPrime = {}
        for num in numSet:
            if num == 1:
                return False
            numToPrime[num] = []
        
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
            for prime in primeList:
                if num % prime == 0:
                    primeDict[prime].add(num)
                    numToPrime[num].append(prime)
                if prime > num:
                    break
        
        for num in numSet:
            getPrimes(num)
        
        visited = set([n])
        level = set([n])
        while level:
            newLevel = set()
            for num in level:
                for prime in numToPrime[num]:
                    new = primeDict[prime].difference(visited)
                    newLevel |= new
                    visited |= new
            level = newLevel
        
        return len(visited) == len(numSet)

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