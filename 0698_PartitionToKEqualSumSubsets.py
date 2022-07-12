# 1st solution
# O(k*2^n) time | O(n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
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

# 2nd solution
# O(2^n*n) time | O(2^n) space
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        nums.sort(reverse = True)

        basket, rem = divmod(sum(nums), k)
        if rem or nums[0] > basket: return False

        dp = [-1] * (1<<N) 
        dp[0] = 0
        for mask in range(1<<N):
            for j in range(N):
                neib = dp[mask ^ (1<<j)]
                if mask & (1<<j) and neib >= 0 and neib + nums[j] <= basket:
                    dp[mask] = (neib + nums[j]) % basket
                    break

        return dp[-1] == 0

