class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 1st solution
        # O(n) time | O(1) space
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                return i
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        
        # 2nd solution
        # O(n) time | O(1) space
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1

        # 3rd solution
        # O(logn) time | O(1) space
        left = 0
        right = len(nums) - 1
        while left <= right:
            if left == right:
                return left
            m = (left + right) // 2
            if nums[m] > nums[m + 1]:
                right = m
            else:
                left = m + 1