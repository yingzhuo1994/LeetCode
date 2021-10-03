class Solution:
    # O(k*2^n) time | O(n) space
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





