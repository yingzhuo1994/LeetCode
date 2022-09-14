# 1st solution
# O(2^n) time | O(2^n) space
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        def dfs(idx, lst):
            ans.append(lst[:])
            if idx == len(nums):
                return
            for i in range(idx, len(nums)):
                if i == idx or nums[i] != nums[i - 1]:
                    dfs(i + 1, lst + [nums[i]])
        
        dfs(0, [])
        return ans