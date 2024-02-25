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