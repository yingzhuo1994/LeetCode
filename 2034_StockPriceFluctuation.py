# 1st solution
class StockPrice:
    def __init__(self):
        self.dic = {}
        self.minHeap = []
        self.maxHeap = []
        self.latest = 0

    def update(self, timestamp: int, price: int) -> None:
        self.dic[timestamp] = price
        heappush(self.minHeap, [price, timestamp])
        heappush(self.maxHeap, [-price, timestamp])
        if timestamp > self.latest:
            self.latest = timestamp
        
    def current(self) -> int:
        return self.dic[self.latest]

    def maximum(self) -> int:
        while self.dic[self.maxHeap[0][1]] != -self.maxHeap[0][0]:
            heappop(self.maxHeap)
        
        return -self.maxHeap[0][0]
        

    def minimum(self) -> int:
        while self.dic[self.minHeap[0][1]] != self.minHeap[0][0]:
            heappop(self.minHeap)
        
        return self.minHeap[0][0]
        


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()