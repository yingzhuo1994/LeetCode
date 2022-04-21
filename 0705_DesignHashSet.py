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
        
# 2nd solution
class MyHashSet:
    def __init__(self):
        self.root = TreeNode(0)
        self.digit = 19

    def add(self, key: int) -> None:
        node = self.findKey(key)
        node.isValid = True  
            
    def remove(self, key: int) -> None:
        node = self.findKey(key)
        node.isValid = False       

    def contains(self, key: int) -> bool:
        node = self.findKey(key)
        return node.isValid
    
    # O(1) time | O(1) space
    def findKey(self, key):
        node = self.root
        k = self.digit
        stack = []
        while k >= 0:
            d = (key >> k) & 1
            stack.append(d)
            if d & 1:
                if not node.right:
                    node.right = TreeNode(1)
                node = node.right
            else:
                if not node.left:
                    node.left = TreeNode(0)
                node = node.left
            k -= 1
        return node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.isValid = False


# 3rd solution, Multiplicative Hash
class MyHashSet: 
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.arr = [[] for _ in range(1<<15)]

    def add(self, key: int) -> None:
        t = self.eval_hash(key)
        if key not in self.arr[t]:
            self.arr[t].append(key)

    def remove(self, key: int) -> None:
        t = self.eval_hash(key)
        if key in self.arr[t]:
            self.arr[t].remove(key)

    def contains(self, key: int) -> bool:
        t = self.eval_hash(key)
        return key in self.arr[t]