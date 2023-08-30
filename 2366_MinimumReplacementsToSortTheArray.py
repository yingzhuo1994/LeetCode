# 1st solution
# O(n) time | O(1) space
from math import ceil
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ret = 0
        prev = nums[n - 1]
        for idx in reversed(range(n - 1)):
            num = nums[idx]

            k = ceil(num / prev)

            # (k - 1) is the minimum number of times you'll have to split
            ret += k - 1
            # (num // k) is the maximal number you can create from splitting (k - 1) times
            prev = num // k
        
        return ret