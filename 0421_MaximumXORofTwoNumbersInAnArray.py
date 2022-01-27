# 1st solution, brute-force
# O(n^2) time | O(1) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        largest = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                x = nums[i] ^ nums[j]
                largest = max(largest, x)
        return largest

# 2nd solution, brute-force
# O(32n) time | O(n) space
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        for i in reversed(range(32)):
            mask |= 1<<i
            found = set([num & mask for num in nums])
                
            start = ans | 1<<i
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
         
        return ans