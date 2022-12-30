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

# 2nd solution
# O(kn) time | O(k + n) space
# where k = len(primes)
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        size = len(primes)
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]