# 1st solution
# O(logN + k) time | O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a, b = 0, len(nums) - 1
        m = (a + b) // 2
        while a <= b:
            if nums[m] == target:
                a = b = m
                break
            elif nums[m] > target:
                b = m -1
            else:
                a = m + 1
            m = (a + b) // 2

        while a > 0 and nums[a - 1] == target:
            a = a - 1

        while b < len(nums) - 1 and nums[b + 1] == target:
            b = b + 1

        return [a, b] if len(nums) > 0 and nums[m] == target else [-1, -1]

# 2nd solution
# O(logN) time | O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                # get the lower mid
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                # get the upper mid
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]

# 3rd solution
# O(log(n)) time | O(1) space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bisect_left(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        left, right = bisect_left(nums, target), bisect_left(nums, target + 1) - 1
        if left > right:
            return [-1, -1]
        
        return [left, right]