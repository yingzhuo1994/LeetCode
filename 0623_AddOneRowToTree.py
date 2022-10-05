# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return root
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        if depth == 2:
            leftNode = TreeNode(val)
            leftNode.left = root.left
            root.left = leftNode
            rightNode = TreeNode(val)
            rightNode.right = root.right
            root.right = rightNode
            return root
        
        root.left = self.addOneRow(root.left, val, depth - 1)
        root.right = self.addOneRow(root.right, val, depth - 1)
        return root
            