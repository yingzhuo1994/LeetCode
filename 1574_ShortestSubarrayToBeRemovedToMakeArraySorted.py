# 1st solution
# O(n * log(n)) time | O(1) space
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        start = 0
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                start = i
            else:
                break
        if start == n - 1:
            return 0
        end = n - 1
        for i in reversed(range(n - 1)):
            if arr[i] <= arr[i + 1]:
                end = i
            else:
                break
        if arr[start] <= arr[end]:
            return end - start - 1

        ans = max(start + 1, n - end)
        for i in range(end, n):
            idx = bisect.bisect_right(arr, arr[i], hi=start+1)
            ans = max(ans, idx + n - i)
            if idx == start:
                break
        
        return n - ans
