# 1st solution
# O(n * log(n)) time | O(1) space 
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            arr[i] = min(arr[i-1] + 1, arr[i])
        return arr[-1]
