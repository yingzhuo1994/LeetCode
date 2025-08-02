# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st soluton
# O(n) time | O(h) space
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left:
            if root.left.val != root.val:
                return False
            left = self.isUnivalTree(root.left)
        else:
            left = True
        
        if root.right:
            if root.right.val != root.val:
                return False
            right = self.isUnivalTree(root.right)
        else:
            right = True
        return left and right