# 1st solution
# O(k^2) time | O(k^2) space
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(start, end, left, right):
            if start > end:
                return 0
            ans = float("inf")
            for i in range(start, end + 1):
                ans = min(ans, dfs(start, i - 1, left, cuts[i]) + dfs(i + 1, end, cuts[i], right))
            ans += right - left
            return ans
        
        cuts.sort()
        
        return dfs(0, len(cuts) - 1, 0, n)