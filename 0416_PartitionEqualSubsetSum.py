# 1st solution, TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        goal = total // 2
        nums.sort()
        return self.dfs(nums, 0, goal)
    
    def dfs(self, nums, idx, goal):
        for i in range(idx, len(nums)):
            if nums[i] == goal:
                return True
            if nums[i] < goal:
                if self.dfs(nums, i + 1, goal - nums[i]):
                    return True
        return False
