# 1st solution
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

# 2nd solution
class StockSpanner:
    def __init__(self):
        self.stock = [[float("inf"), 0]]

    # O(n) time | O(1) space
    def next(self, price: int) -> int:
        count = 1
        while self.stock[-1][0] <= price:
            num, v = self.stock.pop()
            count += v
        self.stock.append([price, count])
        return count