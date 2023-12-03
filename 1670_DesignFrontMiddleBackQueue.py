# 1st solution
class FrontMiddleBackQueue:
    def __init__(self):
        self.length = 0
        self.sentinel = Node(-1)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        self.middle = self.sentinel

    def pushFront(self, val: int) -> None:
        # print("pushFront: ", val)
        node = Node(val)
        node.next = self.sentinel.next
        node.prev = self.sentinel
        self.sentinel.next = node
        node.next.prev = node
        if self.length == 0:
            self.middle = node
        elif self.length & 1:
            self.middle = self.middle.prev
        self.length += 1
        # self.show()
        # print("middle: ", self.middle)
        # print()
        

    def pushMiddle(self, val: int) -> None:
        # print("pushMiddle: ", val)
        # print("middle: ", self.middle)
        node = Node(val)
        if self.length & 1:
            node.next = self.middle
            node.prev = self.middle.prev
            self.middle.prev = node
            node.prev.next = node
        else:
            node.next = self.middle.next
            node.prev = self.middle
            self.middle.next = node
            node.next.prev = node            
        self.middle = node
        self.length += 1       
        # self.show()
        # print("middle: ", self.middle)
        # print()

    def pushBack(self, val: int) -> None:
        # print("pushBack: ", val)
        node = Node(val)
        node.next = self.sentinel
        node.prev = self.sentinel.prev
        self.sentinel.prev = node
        node.prev.next = node
        if self.length == 0:
            self.middle = node
        elif not (self.length & 1):
            self.middle = self.middle.next
        self.length += 1
        # self.show()
        # print("middle: ", self.middle)
        # print()
        

    def popFront(self) -> int:
        if self.length == 0:
            return -1
        node = self.sentinel.next
        # print("popFront: ", node.val)
        if self.length == 1:
            self.middle = self.sentinel
        elif not (self.length & 1):
            self.middle = self.middle.next
        self.remove(node)
        self.length -= 1
        # self.show()
        return node.val
        
    def popMiddle(self) -> int:
        if self.length == 0:
            return -1
        node = self.middle
        # print("popMiddle: ", node.val)
        # print("middle: ", self.middle)
        if self.length & 1:
            self.middle = self.middle.prev
        else:
            self.middle = self.middle.next
        self.remove(node)
        self.length -= 1
        # self.show()
        return node.val        

    def popBack(self) -> int:
        if self.length == 0:
            return -1
        # print("popBack")
        node = self.sentinel.prev
        if self.length == 1:
            self.middle = self.sentinel
        elif self.length & 1:
            self.middle = self.middle.prev
        self.remove(node)
        self.length -= 1
        # self.show()
        return node.val
    
    def remove(self, node):
        # print(node)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
        # print(self.sentinel)
    
    def show(self):
        node = self.sentinel.next
        for i in range(self.length):
            print(i, node)
            node = node.next
        # print()
        
class Node:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None
    def __str__(self):
        return f"val: {self.val}, prev: {self.prev.val if self.prev else None}, next: {self.next.val if self.next else None}"

# 2nd solution
class FrontMiddleBackQueue:
    __slots__ = 'left', 'right'

    def __init__(self):
        self.left = deque()
        self.right = deque()

    # 调整长度，保证 0 <= len(right) - len(left) <= 1
    # 从而保证可以在正中间插入删除元素
    def balance(self):
        if len(self.left) > len(self.right):
            self.right.appendleft(self.left.pop())
        elif len(self.right) > len(self.left) + 1:
            self.left.append(self.right.popleft())

    def pushFront(self, val: int) -> None:
        self.left.appendleft(val)
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.left) < len(self.right):
            self.left.append(val)
        else:
            self.right.appendleft(val)

    def pushBack(self, val: int) -> None:
        self.right.append(val)
        self.balance()

    def popFront(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        val = self.left.popleft() if self.left else self.right.popleft()
        self.balance()
        return val

    def popMiddle(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        if len(self.left) == len(self.right):
            return self.left.pop()
        return self.right.popleft()

    def popBack(self) -> int:
        if not self.right:  # 整个队列为空
            return -1
        val = self.right.pop()
        self.balance()
        return val

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()