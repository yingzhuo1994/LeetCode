# 1st solution
# O(n) time | O(1) space
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[0] >= arr[1] or arr[-2] <= arr[-1]:
            return False
        isAscending = True
        for i in range(len(arr) - 1):
            if isAscending:
                if arr[i] < arr[i + 1]:
                    continue
                else:
                    isAscending = False
            else:
                if arr[i] > arr[i + 1]:
                    continue
                else:
                    return False
        return True
