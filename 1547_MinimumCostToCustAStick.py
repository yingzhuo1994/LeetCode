# 1st solution
# O(k^3) time | O(k^2) space
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

# 2nd solution
# O(k^3) time | O(k^2) space
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        @cache
        def dfs(start, end):
            if start > end:
                return 0
            if end == len(cuts) - 1:
                right = n
            else:
                right = cuts[end + 1]
            if start == 0:
                left = 0
            else:
                left = cuts[start - 1]
            ans = float("inf")
            for i in range(start, end + 1):
                ans = min(ans, dfs(start, i - 1) + dfs(i + 1, end))
            ans += right - left
            return ans
        cuts.sort()

        return dfs(0, len(cuts) - 1)

# 3rd solution, bottom up
# O(k^3) time | O(k^2) space
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = cuts + [0, n]
        k = len(cuts)
        dp = [[0 for _ in range(k)] for _ in range(k)]
        cuts.sort()
        for d in range(2, k):
            for i in range(k - d):
                dp[i][i+d] = min(dp[i][m] + dp[m][i + d] for m in range(i + 1, i + d)) + cuts[i + d] - cuts[i]
        return dp[0][k - 1]