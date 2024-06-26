# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        @cache
        def dfs(i, j, target):
            if i >= j:
                return 0
            count = 0
            if nums[i] + nums[i+1] == target:
                count = max(count, dfs(i+2, j, target) + 1)
            if nums[j] + nums[j-1] == target:
                count = max(count, dfs(i, j-2, target) + 1)
            if nums[i] + nums[j] == target:
                count = max(count, dfs(i + 1, j - 1, target) + 1)
            return count
        n = len(nums)
        res1 = dfs(2, n-1, nums[0] + nums[1])
        if res1 >= n // 2:
            return res1 + 1
        res2 = dfs(1, n-2, nums[0] + nums[n-1])
        if res2 >= n // 2:
            return res2 + 1
        res3 = dfs(0, n-3, nums[n-1] + nums[n-2])
        return max(res1, res2, res3) + 1