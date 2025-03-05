# 1st solution
# O(n^2 * k) time | O(n^2) space
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        # 把 s[i:j+1] 改成回文串的最小修改次数
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def min_change(i: int, j: int) -> int:
            if i >= j:  # 子串只有一个字母，或者子串是空串
                return 0  # 无需修改
            return min_change(i + 1, j - 1) + (1 if s[i] != s[j] else 0)

        # 把 s[:r+1] 切 i 刀，分成 i+1 个子串，每个子串改成回文串的最小总修改次数
        @cache
        def dfs(i: int, r: int) -> int:
            if i == 0:  # 只有一个子串
                return min_change(0, r)
            # 枚举子串左端点 l
            return min(dfs(i - 1, l - 1) + min_change(l, r) 
                       for l in range(i, r + 1))

        return dfs(k - 1, len(s) - 1)
