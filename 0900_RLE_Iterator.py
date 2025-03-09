# 1st solution
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0
        self.pos = 0

    def next(self, n: int) -> int:
        if self.idx >= len(self.encoding):
            return -1
        if self.pos + n > self.encoding[self.idx]:
            k = self.pos + n - self.encoding[self.idx]
            self.idx += 2
            self.pos = 0
            return self.next(k)
        else:
            self.pos += n -1
            num = self.encoding[self.idx + 1]
            self.pos += 1
            return num
            


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)