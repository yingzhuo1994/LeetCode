# 1st solution
class MyLinkedList:

    def __init__(self):
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0
    
    def getNode(self, index):
        if index >= self.size or index < 0:
            return -1
        if index + 1 <= self.size - index:
            cur = self.sentinel
            for _ in range(index + 1):
                cur = cur.next
        else:
            cur = self.sentinel
            for _ in range(self.size - index):
                cur = cur.prev
        return cur        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        node = self.getNode(index)
        return node.val
        
    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.prev = self.sentinel
        node.next = self.sentinel.next
        node.next.prev = node
        node.prev.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        node.prev = self.sentinel.prev
        node.next = self.sentinel
        node.next.prev = node
        node.prev.next = node   
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        node = Node(val)
        nextNode = self.getNode(index)
        node.prev = nextNode.prev
        node.next = nextNode
        node.next.prev = node
        node.prev.next = node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        node = self.getNode(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.size -= 1
        
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)