# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True] * (right + 1)
        primes[1] = False
        for i in range(2, right + 1):
            if primes[i]:
                primes[i+i:right+1:i] = [False] * len(primes[i+i:right+1:i])
        candidates = []
        for num in range(left, right + 1):
            if primes[num]:
                candidates.append(num)
        ans = [-1, -1]
        for i in range(1, len(candidates)):
            if ans[0] < 0 or candidates[i] - candidates[i - 1] < ans[1] - ans[0]:
                ans = candidates[i-1:i+1]
        return ans