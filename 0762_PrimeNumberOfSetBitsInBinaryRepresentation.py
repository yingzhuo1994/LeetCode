
# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        n = len(bin(right)) - 2
        primes = [True for _ in range(n + 1)]
        primes[0] = False
        primes[1] = False
        for num in range(2, n):
            if primes[num]:
                primes[2 * num::num] = [False] * len(primes[2 * num::num])
        ans = 0
        for num in range(left, right + 1):
            k = bin(num)[2:].count("1")
            ans += primes[k]
        return ans