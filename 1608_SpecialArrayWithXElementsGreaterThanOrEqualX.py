# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        start = 0
        end = n
        while start <= end:
            mid = start + (end - start) // 2
            idx = bisect.bisect_left(nums, mid)
            count = n - idx
            if count < mid:
                end = mid - 1
            elif count > mid:
                start = mid + 1
            else:
                return mid
        return -1