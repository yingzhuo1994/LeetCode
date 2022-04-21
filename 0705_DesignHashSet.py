# 1st solution
class MyHashSet:

    def __init__(self):
        self.stack = []

    def add(self, key: int) -> None:
        index = self.findKey(key)
        if index >= len(self.stack) or self.stack[index] != key:
            self.stack.insert(index, key)

    def remove(self, key: int) -> None:
        index = self.findKey(key)
        if index < len(self.stack) and self.stack[index] == key:
            self.stack.pop(index)


    def contains(self, key: int) -> bool:
        index = self.findKey(key)
        return index < len(self.stack) and self.stack[index] == key

    def findKey(self, key):
        left, right = 0, len(self.stack) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.stack[mid] < key:
                left = mid + 1
            elif self.stack[mid] > key:
                right = mid - 1
            else:
                return mid
        return left
        
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)