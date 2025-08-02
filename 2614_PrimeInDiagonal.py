# 1st solution
# O(n + N * log(log(N))) time | O(N) space
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        N = max(map(max, nums))
        primes = [True] * (N + 1)
        primes[1] = False
        for i in range(2, N + 1):
            if primes[i]:
                primes[i+i:N+1:i] = [False] * len(primes[i+i:N+1:i])
        ans = 0
        n = len(nums)
        for i in range(n):
            if primes[nums[i][i]]:
                ans = max(ans, nums[i][i])
            if primes[nums[i][n-1-i]]:
                ans = max(ans, nums[i][n-1-i])
        return ans