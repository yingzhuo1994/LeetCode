# 1st solution
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.idx = 0

    def push(self, x: int) -> None:
        if self.idx < len(self.stack):
            self.stack[self.idx] = x
            self.idx += 1

    def pop(self) -> int:
        if self.idx > 0:
            val = self.stack[self.idx - 1]
            self.idx -= 1
        else:
            val = -1
        return val
        
    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.idx)):
            self.stack[i] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)