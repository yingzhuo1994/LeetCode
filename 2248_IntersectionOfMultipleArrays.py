# 1st solution
# O(mn) time | O(n)
# where m is the length of nums, and n is the average length of nums[i]
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        candidates = set(nums[0])
        for i in range(1, len(nums)):
            level = set()
            for num in nums[i]:
                if num in candidates:
                    level.add(num)
            candidates = level
        ans = sorted(list(candidates))
        return ans