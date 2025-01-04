# 1st solution
# O(n) time | O(1) space
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        direction = 0
        ans = 0
        start = 0
        for i in range(1, n):
            if direction == 0:
                if arr[i] > arr[i - 1]:
                    direction = 1
                else:
                    start = i
            elif direction == 1:
                if arr[i] < arr[i - 1]:
                    direction = -1
                    ans = max(ans, i - start + 1)
                elif arr[i] == arr[i - 1]:
                    direction = 0
                    start = i
            else:
                if arr[i] < arr[i - 1]:
                    ans = max(ans, i - start + 1)
                elif arr[i] > arr[i - 1]:
                    start = i - 1
                    direction = 1
                else:
                    direction = 0
                    start = i
        return ans