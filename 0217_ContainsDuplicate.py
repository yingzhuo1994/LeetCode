# 1st solution
# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

# 2nd sorting solution
# O(nlogn) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

# 3rd solution
# O(n) time | O(n) space
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen: return True 
            seen.add(x)
        return False