# 1st solution
class MyHashMap:
    def __init__(self):
        self.root = TreeNode(0)
        self.digit = 20

    def put(self, key: int, value: int) -> None:
        node = self.findKey(key)
        node.ans = value
        node.isValid = True
        
    def get(self, key: int) -> int:
        node = self.findKey(key)
        if node.isValid:
            return node.ans
        else:
            return -1

    def remove(self, key: int) -> None:
        node = self.findKey(key)
        node.isValid = False
    
    def findKey(self, key):
        k = self.digit
        node = self.root
        while k >= 0:
            d = (key >> k) & 1
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
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.isValid = False
        self.ans = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)