# 1st solution, TLE
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
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

# 2nd solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, n = sum(nums), len(nums)
        if target & 1: return False
        target >>= 1
        dp = [True] + [False]*target
        for x in nums:
            dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
            if dp[target]: return True
        return False

# 3rd solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False
        nums.sort(reverse=True)
        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s >> 1)