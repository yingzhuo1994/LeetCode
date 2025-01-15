# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0
        while nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            z = min(x, y) * 2 + max(x, y)
            ans += 1
            heappush(nums, z)
        return ans