# 1st solution, dynamic programming
# O(n*target) time | O(n*target) space
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        maxNum = max(nums)
        if total & 1:
            return False
        
        target = total // 2
        if maxNum > target:
            return False
        
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[n - 1][target]

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