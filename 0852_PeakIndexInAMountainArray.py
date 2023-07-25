# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 1, n - 2
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            elif arr[mid - 1] > arr[mid]:
                right = mid - 1
            else:
                return mid
        return left