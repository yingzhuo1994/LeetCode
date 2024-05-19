# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        g = [[] for _ in nums]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> (int, int):
            f0, f1 = 0, -inf  # f[x][0] 和 f[x][1]
            for y in g[x]:
                if y != fa:
                    r0, r1 = dfs(y, x)
                    f0, f1 = max(f0 + r0, f1 + r1), max(f1 + r0, f0 + r1)
            return max(f0 + nums[x], f1 + (nums[x] ^ k)), max(f1 + nums[x], f0 + (nums[x] ^ k))
        return dfs(0, -1)[0]