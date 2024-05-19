# 1st solution
# O(n) time | O(n) space
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in nums]
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(x: int, fa: int) -> (int, int):
            f0, f1 = 0, -inf  # f[x][0] 和 f[x][1]
            for y in graph[x]:
                if y != fa:
                    r0, r1 = dfs(y, x)
                    f0, f1 = max(f0 + r0, f1 + r1), max(f1 + r0, f0 + r1)
            return max(f0 + nums[x], f1 + (nums[x] ^ k)), max(f1 + nums[x], f0 + (nums[x] ^ k))
        return dfs(0, -1)[0]


# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, _: List[List[int]]) -> int:
        f0, f1 = 0, -inf
        for x in nums:
            f0, f1 = max(f0 + x, f1 + (x ^ k)), max(f1 + x, f0 + (x ^ k))
        return f0