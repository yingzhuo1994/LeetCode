# 1st solution
# O(limit^2) time : O(1) space
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def dfs(k, left):
            if k == 1:
                return left <= limit
            ans = 0
            for i in range(min(left, limit) + 1):
                ans += dfs(k-1, left - i)
            return ans
        return dfs(3, n)