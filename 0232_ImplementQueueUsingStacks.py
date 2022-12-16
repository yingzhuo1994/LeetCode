# 1st solution
class MyQueue:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.size += 1
        
    def pop(self) -> int:
        self.stack.reverse()
        val = self.stack.pop()
        self.stack.reverse()
        self.size -= 1
        return val
        
    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return self.size == 0
        
# 2nd solution
class MyQueue:
    def __init__(self):
        self.stack = []
        self.start = 0
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        
    def pop(self) -> int:
        val = self.stack[self.start]
        self.start += 1
        return val
        
    def peek(self) -> int:
        return self.stack[self.start]
        
    def empty(self) -> bool:
        return len(self.stack) == self.start
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()