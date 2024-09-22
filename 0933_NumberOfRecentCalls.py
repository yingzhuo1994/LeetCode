# 1st solution
class RecentCounter:

    def __init__(self):
        self.minHeap = []

    # O(log(n)) time
    def ping(self, t: int) -> int:
        heappush(self.minHeap, t)
        while self.minHeap and self.minHeap[0] < t - 3000:
            heappop(self.minHeap)
        return len(self.minHeap)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)