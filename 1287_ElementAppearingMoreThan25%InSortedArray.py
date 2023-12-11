# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        while start < len(arr):
            num = arr[start]
            idx = bisect.bisect_right(arr, num)
            length = idx - start
            if length * 4 > n:
                return num
            start = idx
        return -1