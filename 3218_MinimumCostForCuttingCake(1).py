# 1st solution
# O(mn) time | O(mn) space
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n -1:
                return 0
            if i == m - 1:
                return m * verticalCut[j] + dfs(i, j + 1)
            elif j == n - 1:
                return n * horizontalCut[i] + dfs(i + 1, j)
            else:
                return min((i + 1) * verticalCut[j] + dfs(i, j + 1), (j + 1) * horizontalCut[i] + dfs(i + 1, j))
        return dfs(0, 0)