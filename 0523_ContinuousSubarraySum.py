# 1st solution, TLE
# O(n^2) time | O(n) space
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2:
            return False
        sums = nums[:]
        for i in range(n - 1):
            sums[i + 1] += sums[i]
        
        for i in range(1, n):
            if sums[i] % k == 0:
                return True
            for j in range(i - 1):
                diff = sums[i] - sums[j]
                if diff % k == 0:
                    return True
        return False