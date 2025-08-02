# 1st solution
# O(2^n) time | O(2^n) space
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for num in nums:
            mx |= num
        
        visited = set()
        n = len(nums)
        @cache
        def dfs(idx, mask, val=0):
            if idx == n:
                if val == mx:
                    visited.add(mask)
                return
            dfs(idx + 1, mask | (1 << idx), val | nums[idx])
            dfs(idx + 1, mask, val)
        dfs(0 ,0, 0)
        ans = len(visited)
        return ans