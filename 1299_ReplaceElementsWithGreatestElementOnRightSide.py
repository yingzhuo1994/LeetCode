# 1st solution
# O(n) time | O(1) space
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        val = arr[-1]
        for i in reversed(range(n - 1)):
            ans[i] = val
            val = max(val, arr[i])
        return ans