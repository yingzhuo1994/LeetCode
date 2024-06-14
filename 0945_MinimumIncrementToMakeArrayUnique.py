# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        last = -1
        ans = 0
        for num in nums:
            if num <= last:
                ans += last + 1 - num
                last += 1
            else:
                last = num
        return ans