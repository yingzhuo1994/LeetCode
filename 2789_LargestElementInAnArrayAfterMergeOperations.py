# 1st solution
# O(n) time | O(1) space
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        while len(nums) >= 2:
            if nums[-1] < nums[-2]:
                ans = max(ans, nums.pop())
            else:
                nums[-2] += nums[-1]
                nums.pop()
                ans = max(ans, nums[-1])
        return ans

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int: 
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] <= nums[i]:
                nums[i - 1] = nums[i - 1] + nums[i]
        
        return nums[0]