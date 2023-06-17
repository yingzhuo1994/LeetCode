# 1st solution
# O(m * (m + n) * log(n)) time | O(m * (m + n)) space
# where m = len(arr1), n = len(arr2)
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

            new = dfs(idx + 1, arr2[i]) + 1
            ans = min(ans, new)
            return ans
        
        ans = dfs(0, -1)
        if ans == float("inf"):
            return -1
        else:
            return ans