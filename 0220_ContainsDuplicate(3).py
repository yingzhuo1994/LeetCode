# 1st solution
# O(nd) time | O(1) space
# where n = len(nums), and d = indexDiff
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + indexDiff + 1, n)):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False


