class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 1st solution
        # O(lonN + k) time | O(1) space
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
        if not nums:
            return [-1, -1]

        def bisect_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def bisect_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [bisect_left(nums, target), bisect_right(nums, target)]
