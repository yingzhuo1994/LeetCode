# 1st solution
# O(n) time | O(1) space
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = [True for i in range(101)]
        primes[0] = False
        primes[1] = False
        for num in range(2, 101):
            if primes[num]:
                primes[num+num::num] = [False] * len(primes[num+num::num])


        left = 0
        for i, num in enumerate(nums):
            if primes[num]:
                left = i
                break

        right = len(nums) - 1
        for i in reversed(range(len(nums))):
            num = nums[i]
            if primes[num]:
                right = i
                break
        
        return right - left 
