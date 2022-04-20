# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push(root)

    def next(self) -> int:
        node = self.stack.pop()
        value = node.val
        self.push(node.right)
        return value
        
    def hasNext(self) -> bool:
        return len(self.stack) > 0
    
    def push(self, node):
        while node:
            self.stack.append(node)
            node = node.left
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()