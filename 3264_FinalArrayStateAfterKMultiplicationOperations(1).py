# 1st solution
# O((n + k) * log(n)) time | O(n) space
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minHeap = []
        for i, num in enumerate(nums):
            heappush(minHeap, [num, i])
        for _ in range(k):
            num, i = heappop(minHeap)
            nums[i] = num * multiplier
            heappush(minHeap, [nums[i], i])
        return nums