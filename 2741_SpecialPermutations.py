# 1st solution
# O(n) time | O(n * 2^n) space
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                    graph[i].append(j)
                    graph[j].append(i)
        ans = 0
        @cache
        def dfs(idx, mask):
            if (1 << idx) & mask:
                return 0
            mask |= 1 << idx
            if mask == (1 << n) - 1:
                return 1
            count = 0
            for neig in graph[idx]:
                count += dfs(neig, mask)
            return count
        for i in range(n):
            ans += dfs(i, 0)
            ans %= MOD
        return ans