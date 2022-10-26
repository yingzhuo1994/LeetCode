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

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            # if the remainder s % k occurs for the first time
            target = s % k
            if target not in hash_map:
                hash_map[target] = i + 1
            # if the subarray size is at least two
            elif hash_map[target] < i:
                return True
        return False