# 1st solution
# O(n) time | O(n) space
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixSet = set()
        prefixDiff = [1 for _ in range(n)]
        for i, num in enumerate(nums):
            prefixSet.add(num)
            prefixDiff[i] = len(prefixSet)
        suffixSet = set()
        suffixDiff = [0 for _ in range(n)]
        for i in reversed(range(n)):
            num = nums[i]
            suffixDiff[i] = len(suffixSet)
            suffixSet.add(num)
        
        ans = [a - b for a, b in zip(prefixDiff, suffixDiff)]
        return ans