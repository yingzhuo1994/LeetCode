# 1st solution
# O(n) time | O(1) space
primes = [2]
for i in range(3, 1001):
    isPrime = True
    for num in primes:
        if i % num == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(i)
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        for i, num in enumerate(nums):
            diff = num - prev
            if diff <= 0:
                return False
            idx = bisect.bisect_left(primes, diff) - 1
            if idx < 0:
                prev = num
                continue
            prev = num - primes[idx]
        return True
