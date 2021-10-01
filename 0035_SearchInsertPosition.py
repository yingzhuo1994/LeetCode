class Solution:
    # 1st solution
    # O(log(n)) time | O(1) space
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

    # 2nd solution
    # O(log(n)) time | O(1) space
    def searchInsert(self, nums: List[int], target: int) -> int:
        beg, end = 0, len(nums)
        while beg < end:
            mid = (beg + end)//2
            if nums[mid] >= target:
                end = mid
            else:
                beg = mid + 1
        return beg