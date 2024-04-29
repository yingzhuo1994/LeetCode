# 1st solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        val = nums[0]
        for i in range(1, len(nums)):
            val ^= nums[i]
        
        ans = 0
        for i in range(32):
            a = (val >> i) & 1
            b = (k >> i) & 1
            if a != b:
                ans += 1
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return reduce(xor, nums, k).bit_count()