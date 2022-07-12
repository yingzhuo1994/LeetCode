# 1st solution
# O(2^n*n) time | O(2^n) space
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        N = len(matchsticks)
        matchsticks.sort(reverse = True)

        basket, rem = divmod(sum(matchsticks), k)
        if rem or matchsticks[0] > basket: return False

        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                neib = dp[mask ^ (1<<j)]
                if mask & (1<<j) and neib >= 0 and neib + matchsticks[j] <= basket:
                    dp[mask] = (neib + matchsticks[j]) % basket
                    break

        return dp[-1] == 0

# 2nd solution
# O(2^n*n) time | O(2^n) space
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        k = 4
        nums = matchsticks
        total = sum(nums)
        if len(nums) < k or total % k != 0:
            return False
        goal = total // k
        
        nums.sort(reverse=True)
        visited = [False] * len(nums)
        
        def can_partition(rest_k, cur_sum=0, next_index=0):
            if rest_k == 1:
                return True
            
            if cur_sum == goal:
                return can_partition(rest_k - 1)
            
            for i in range(next_index, len(nums)):
                if not visited[i] and cur_sum + nums[i] <= goal:
                    visited[i] = True
                    if can_partition(rest_k, cur_sum + nums[i], i + 1):
                        return True
                    visited[i] = False
            return False 

        return can_partition(k)