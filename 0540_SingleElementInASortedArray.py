# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if mid & 1:
                if nums[mid - 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid
        return nums[left]

# 2nd solution, simplified
# O(log(n)) time | O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # odd xor 1 = odd-1
            # even xor 1 = even+1
            if nums[mid] == nums[mid ^ 1]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

# 3rd solution
# O(log(n)) time | O(1) space
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n - 1) // 2
        left, right = 0, k
        while left < right:
            mid = left + (right - left) // 2
            idx = mid * 2
            if idx + 1 < n:
                if nums[idx + 1] == nums[idx]:
                    left = mid + 1
                else:
                    right = mid
            else:
                return nums[idx]
        return nums[left * 2]