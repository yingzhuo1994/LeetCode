# 1st solution
# O(n) time | O(n) space
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        lst = [0] * len(nums)
        lst[0] = nums[0]
        lst[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            lst[i] = max(lst[i-1], nums[i] + lst[i-2])
        return lst[-1]

# 2nd solution
# O(n) time | O(1) sapce
class Solution:
    def rob(self, nums: List[int]) -> int:
        front, back = 0, 0
        for num in nums:
            front, back = back, max(back, num + front)
        return back