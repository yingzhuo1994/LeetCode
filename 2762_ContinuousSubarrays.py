# 1st solution
# O(n * log(n)) time | O(n) space 
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        minHeap = []
        maxHeap = []
        ans = 0
        start = 0
        for i, num in enumerate(nums):
            heappush(minHeap, [num, i])
            heappush(maxHeap, [-num, i])
            while True:
                diff = -maxHeap[0][0] - minHeap[0][0]
                if diff <= 2:
                    ans += i - start + 1
                    break
                start += 1
                while maxHeap[0][1] < start:
                    heappop(maxHeap)
                while minHeap[0][1] < start:
                    heappop(minHeap)
        return ans