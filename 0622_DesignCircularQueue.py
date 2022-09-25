class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.sentinel = Node(0)
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
        
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        last = self.sentinel.prev
        node = Node(value)
        last.next = node
        node.prev = last

        node.next = self.sentinel
        self.sentinel.prev = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        node = self.sentinel.next
        self.sentinel.next = node.next
        node.next.prev = self.sentinel

        node.prev = None
        node.next = None
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.sentinel.next.value
       

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.sentinel.prev.value

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == self.capacity

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()