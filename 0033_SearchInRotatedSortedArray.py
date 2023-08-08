# 1st solution
# O(log(n)) time | O(1) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a, b = 0, len(nums) - 1
        while a <= b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            if nums[a] <= nums[m]:
                if nums[a] <= target < nums[m]:
                    b = m - 1
                else:
                    a = m + 1
            else:
                if nums[m] < target <= nums[b]:
                    a = m + 1
                else:
                    b = m -1
        return -1

# 2nd solution
# O(log(n)) time | O(log(n)) space
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        def helper(nums, start, end):
            if start > end:
                return -1
            if nums[start] < nums[end]:
                while start <= end:
                    mid = start + (end - start) // 2
                    if nums[mid] < target:
                        start = mid + 1
                    elif nums[mid] > target:
                        end = mid - 1
                    else:
                        return mid
                return -1
            else:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                ans = helper(nums, start, mid - 1)
                if ans != -1:
                    return ans
                else:
                    return helper(nums, mid + 1, end)
        
        return helper(nums, left, right)