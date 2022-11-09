class StockSpanner:
    def __init__(self):
        self.stock = [float("inf")]
        self.span = [0]

    # O(n) time | O(1) space
    def next(self, price: int) -> int:
        count = 1
        idx = len(self.stock) - 1
        while idx >= 0:
            if self.stock[idx] <= price:
                count += self.span[idx]
                idx -= self.span[idx]
            else:
                break
        self.stock.append(price)
        self.span.append(count)
        return count

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)