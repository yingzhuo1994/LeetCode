# 1st solution, Sieve of Eratosthenes
# O(nloglogn) time | O(n) space
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

# 2nd solution, linear prime sieve
# O(n) time | O(n) space
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        tables = [False] * n
        primes = []
        for i in range(2, n):
            if not tables[i]:
                primes.append(i)
            for prime in primes:
                if prime * i >= n:
                    break
                tables[prime * i] = True
                if i % prime == 0:
                    break
        return len(primes)