# 1st solution
# O(n * log(n)) time | O(n) space
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        def enough(k):
            return all(2 * nums[i] <= nums[-(k - i)] for i in range(k))

        nums.sort()
        n = len(nums)
        start = 0
        end = n // 2
        while start <= end:
            mid = start + (end - start) // 2
            if enough(mid):
                start = mid + 1
            else:
                end = mid - 1
        return end