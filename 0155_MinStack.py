class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val > self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            start = 0
            end = len(self.min_stack) - 1
            while start < end:
                mid = (start + end) // 2
                midVal = self.min_stack[mid]
                if val == midVal:
                    end = mid
                    break
                elif val > midVal:
                    start = mid + 1
                else:
                    end = mid
            self.min_stack.insert(end, val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.min_stack.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
