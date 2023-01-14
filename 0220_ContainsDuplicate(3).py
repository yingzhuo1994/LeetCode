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

# 2nd solution
# O(n * log(k)) time | O(k) space
# where n = len(nums), and k = indexDiff
from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        SList = SortedList()
        k = indexDiff
        t = valueDiff
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False

# 3rd solution
# O(n) time | O(k) space
# where n = len(nums), and d = indexDiff
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        k = indexDiff
        t = valueDiff

        seen = {}
        for i, x in enumerate(nums): 
            bkt = x // (t + 1)
            if bkt in seen and i - seen[bkt][0] <= k: return True 
            if bkt-1 in seen and i - seen[bkt-1][0] <= k and abs(x - seen[bkt-1][1]) <= t: return True 
            if bkt+1 in seen and i - seen[bkt+1][0] <= k and abs(x - seen[bkt+1][1]) <= t: return True 
            seen[bkt] = (i, x) 
        return False 