# 1st solution
# O(mn) time | O(mn) space
# where n = len(floor), m = numCarpets 
class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        floor = list(map(int, floor))  # 避免在 dfs 中频繁调用 int()
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（一行代码实现记忆化）
        def dfs(i: int, j: int) -> int:
            if j < carpetLen * i:  # 剩余砖块可以全部覆盖
                return 0
            if i == 0:
                return dfs(i, j - 1) + floor[j]
            return min(dfs(i, j - 1) + floor[j], dfs(i - 1, j - carpetLen))
        return dfs(numCarpets, len(floor) - 1)