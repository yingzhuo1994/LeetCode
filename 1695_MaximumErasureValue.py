# 1st solution
# O(n) time | O(n) space
from itertools import accumulate
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        arraySum = [0] + list(accumulate(nums))
        ans = 0
        dic = {}
        start = 0
        for i, num in enumerate(nums):
            if num in dic and dic[num] >= start:
                start = dic[num] + 1
            dic[num] = i
            curTotal = arraySum[i+1] - arraySum[start]
            ans = max(ans, curTotal)
        return ans

# 2nd solution
# O(n) time | O(n) space
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        dic = {}
        start = 0
        curTotal = 0
        for i, num in enumerate(nums):
            if num in dic and dic[num] >= start:
                for j in range(start, dic[num] + 1):
                    curTotal -= nums[j]
                start = dic[num] + 1
            dic[num] = i
            curTotal += nums[i]
            ans = max(ans, curTotal)
        return ans