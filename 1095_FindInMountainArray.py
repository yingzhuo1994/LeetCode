# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# 1st solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        start, end = 0, n - 1
        self.ans = float("inf")
        self.dic = {}

        def query(idx):
            if idx not in self.dic:
                self.dic[idx] = mountain_arr.get(idx)
            return self.dic[idx]

        def helper(start, end):
            if start > end:
                return float("inf")
            elif start == end:
                value = query(start)
                if value == target:
                    self.ans = min(self.ans, start)
                return
            else:
                mid = start + (end - start) // 2
                midValue = query(mid)
                midValue2 = query(mid + 1)
                diff = midValue2 - midValue
                if diff > 0:
                    if target > midValue:
                        helper(mid + 1, end)
                    elif target < midValue:
                        helper(start, mid - 1)
                        endValue = query(end)
                        if endValue < midValue:
                            helper(mid + 1, end)
                    else:
                        helper(mid, mid)
                else:
                    if target < midValue:
                        helper(mid + 1, end)
                        startValue = query(start)
                        if startValue < midValue:
                            helper(start, mid - 1)
                    elif target > midValue:
                        helper(start, mid - 1)
                    else:
                        helper(mid, mid)
                        helper(start, mid - 1)
        
        helper(start, end)
        return self.ans if self.ans != float("inf") else -1
        
        





