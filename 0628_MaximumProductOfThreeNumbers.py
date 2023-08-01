# 1st solution, TLE
# O(n^3) time | O(1) space
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans = max(ans, nums[i] * nums[j] * nums[k])
        return ans

# 3nd solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        positive = [num for num in nums if num >= 0]
        negtive = [num for num in nums if num < 0]

        positive.sort()
        negtive.sort()

        ans = float("-inf")
        for num in nums:
            if num == 0:
                ans = 0

        if len(positive) >= 3:
            ans = max(ans, positive[-1] * positive[-2] * positive[-3])
        
        if len(negtive) >= 3:
            ans = max(ans, negtive[-1] * negtive[-2] * negtive[-3])
        
        if len(positive) >= 1 and len(negtive) >= 2:
            ans = max(ans, negtive[0] * negtive[1] * positive[-1])
        
        if len(positive) >= 2 and len(negtive) >= 1:
            ans = max(ans, positive[0] * positive[1] * negtive[-1])
        
        return ans
            
