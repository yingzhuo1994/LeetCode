primes = [2]
N = int(math.sqrt(10**9)) + 1
for i in range(3, N + 1):
    isPrime = True
    for p in primes:
        if i % p == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)

# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def query(n):
            t = int(math.sqrt(n))
            return bisect.bisect_right(primes, t)
        count = query(r) - query(l - 1)
        return r - l + 1 - count