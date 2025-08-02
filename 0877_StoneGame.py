# 1st solution
# O(n^2) time | O(n^2) space 
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(start, end):
            if start == end:
                return piles[start]
            left = piles[start] - dfs(start + 1, end)
            right = piles[end] - dfs(start, end - 1)
            return max(left, right)
        n = len(piles)
        return dfs(0, n - 1) > 0