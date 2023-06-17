# 1st solution, TLE
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def dfs(idx, prev):
            if idx == len(arr1):
                return 0
            if arr1[idx] > prev:
                ans = dfs(idx + 1, arr1[idx])
            else:
                ans = float("inf")
            i = bisect.bisect_right(arr2, prev)
            if i >= len(arr2):
                return ans
            for j in range(i, len(arr2)):
                new = dfs(idx + 1, arr2[j]) + 1
                ans = min(ans, new)
            return ans
        
        ans = dfs(0, -1)
        if ans == float("inf"):
            return -1
        else:
            return ans