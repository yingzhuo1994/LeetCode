# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        s = list(accumulate(stones, initial=0))  # 前缀和
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == j:  # 递归边界
                return 0
            return max(s[j + 1] - s[i + 1] - dfs(i + 1, j), s[j] - s[i] - dfs(i, j - 1))
        ans = dfs(0, len(stones) - 1)
        dfs.cache_clear()  # 防止爆内存
        return ans

# 2nd solution
# O(n^2) time | O(n) space
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        s = list(accumulate(stones, initial=0))
        f = [0] * n
        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                f[j] = max(s[j + 1] - s[i + 1] - f[j], s[j] - s[i] - f[j - 1])
        return f[-1]


# 3rd solution
# O(n^2) time | O(n^2) space
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        s = list(accumulate(stones, initial=0))
        f = [[0] * n for _ in range(n)]
        for i in reversed(range(n - 1)):
            for j in range(i + 1, n):
                f[i][j] = max(s[j + 1] - s[i + 1] - f[i + 1][j], s[j] - s[i] - f[i][j - 1])
        return f[0][-1]