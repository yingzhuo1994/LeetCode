# 1st solution
# O(n*log(n)) time | O(n) space
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.maxHeap = []
        self.kIdx = k
        for num in nums:
            heapq.heappush(self.minHeap, num)
            self.check()
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        self.check()
        return -self.maxHeap[0]

    def check(self):    
        if len(self.minHeap) ==  self.kIdx:
            value = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -value)
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)