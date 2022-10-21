# O(n) time | O(n) space
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        numDic = {}
        for i, num in enumerate(nums):
            if num in numDic and i - numDic[num] <= k:
                return True
            numDic[num] = i
        return False