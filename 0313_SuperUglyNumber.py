# 1st solution
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        visited = set()
        stack = [1]
        count = 1
        while count < n:
            num = heappop(stack)
            for prime in primes:
                val = num * prime
                if val not in visited:
                    visited.add(val)
                    heappush(stack, val)
            count += 1
        
        return heappop(stack)