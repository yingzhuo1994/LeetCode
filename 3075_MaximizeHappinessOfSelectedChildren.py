# 1st solution
# O(k * log(n)) time | O(n) space
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        minHeap = [-val for val in happiness]
        heapify(minHeap)
        ans = 0
        for i in range(k):
            val = -heappop(minHeap)
            val = max(0, val - i)
            ans += val
        return ans