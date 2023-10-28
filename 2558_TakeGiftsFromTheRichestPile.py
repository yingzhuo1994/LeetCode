# 1st solution
# O((n + k) * log(n)) time | O(n) space
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        minHeap = [-gift for gift in gifts]
        heapify(minHeap)
        for _ in range(k):
            gift = -heappop(minHeap)
            newGift = math.floor(math.sqrt(gift))
            heappush(minHeap, - newGift)
        return -sum(minHeap)