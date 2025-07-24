# 1st solution
# O(n^2) time | O(n) space
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        xor, in_, out = [0] * n, [0] * n, [0] * n
        clock = 0
        def dfs(x: int, fa: int) -> None:
            nonlocal clock
            clock += 1
            in_[x] = clock  # 递
            xor[x] = nums[x]
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
                    xor[x] ^= xor[y]
            out[x] = clock  # 归
        dfs(0, -1)

        # 判断 x 是否为 y 的祖先
        def is_ancestor(x: int, y: int) -> bool:
            return in_[x] < in_[y] <= out[x]

        ans = inf
        # 枚举：删除 x 与 x 父节点之间的边，删除 y 与 y 父节点之间的边
        for x in range(2, n):
            for y in range(1, x):
                if is_ancestor(x, y):  # x 是 y 的祖先
                    a, b, c = xor[y], xor[x] ^ xor[y], xor[0] ^ xor[x]
                elif is_ancestor(y, x):  # y 是 x 的祖先
                    a, b, c = xor[x], xor[x] ^ xor[y], xor[0] ^ xor[y]
                else:  # x 和 y 分别属于两棵不相交的子树
                    a, b, c = xor[x], xor[y], xor[0] ^ xor[x] ^ xor[y]
                ans = min(ans, max(a, b, c) - min(a, b, c))
                if ans == 0:  # 不可能变小
                    return 0  # 提前返回
        return ans