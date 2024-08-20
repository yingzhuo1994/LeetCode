# 1st solution
# O(k * log(k)) time | O(k * log(k)) space
class Solution:
    def waysToReachStair(self, k: int) -> int:
        @cache
        def dfs(i, jump, back):
            count = 0
            if i == k:
                count += 1
            elif i - 1 > k:
                return float("-inf")
            val = dfs(i + pow(2, jump), jump + 1, False)
            if val != float("-inf"):
                count += val
            if i == 0 or back:
                return count
            val = dfs(i - 1, jump, True)
            if val != float("-inf"):
                count += val
            return count
        ans = dfs(1, 0, False)
        return ans