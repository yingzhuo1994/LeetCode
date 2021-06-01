class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1st solution
        # O(n) time | O(n) space
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
        if len(nums) == 1:
            return nums[0]
        front = nums[0]
        back = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            front, back = back, max(back, nums[i] + front)
        return back