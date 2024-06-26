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


# 2nd solution
# O(1) time : O(1) space
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def c2(n: int) -> int:
            return n * (n - 1) // 2 if n > 1 else 0
        return c2(n + 2) - 3 * c2(n - limit + 1) + 3 * c2(n - 2 * limit) - c2(n - 3 * limit - 1)