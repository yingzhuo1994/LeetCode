# 1st solution
# O(n) time | O(n) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n <= 3:
            return max(nums)
        
        def helper(nums):
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[:2])
            containsFisrt = False
            if dp[0] + nums[2] > dp[1]:
                dp[2] = dp[0] + nums[2]
                containsFisrt = True
            else:
                dp[2] = dp[1]
            
            for i in range(3, n - 1):
                if dp[i-2] + nums[i] > dp[i-1]:
                    dp[i] = dp[i-2] + nums[i]
                else:
                    dp[i] = dp[i-1]

            if not containsFisrt:
                i = n - 1
                if dp[i-2] + nums[i] > dp[i-1]:
                    dp[i] = dp[i-2] + nums[i]
                else:
                    dp[i] = dp[i-1]
            return max(dp)
        return max(helper(nums), helper(nums[::-1]))

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n <= 3:
            return max(nums)
        
        def rob_helper(nums, lo, hi):
            dp1, dp2 = 0, 0
            for i in range(lo, hi+1):
                num = nums[i]
                dp1, dp2 = dp2, max(dp1 + num, dp2)          
            return dp2
    
        return max(rob_helper(nums, 0, n-2), rob_helper(nums, 1, n-1))