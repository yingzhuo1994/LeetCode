# 1st solution
class SeatManager:

    def __init__(self, n: int):
        self.minHeap = [i for i in range(1, n + 1)]
        heapify(self.minHeap)
    
    # O(log(n)) time
    def reserve(self) -> int:
        seat = heappop(self.minHeap)
        return seat
    
    # O(log(n)) time
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.minHeap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)