# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return None
                        
            left = node.left
            right = node.right
            node.left = None
            if left:
                tail = helper(left)
                node.right = left
                node = tail
            if not right:
                return node
            node.right = right
            return helper(node.right)
        helper(root)