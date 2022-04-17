# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.leftMost = TreeNode(0)
        self.rightMost = self.leftMost
        self.inOrderTraverse(root)
        return self.leftMost.right

    def inOrderTraverse(self, node):
        if not node:
            return 
        self.inOrderTraverse(node.left)
        self.rightMost.right = node
        node.left = None
        self.rightMost = node
        self.inOrderTraverse(node.right)
