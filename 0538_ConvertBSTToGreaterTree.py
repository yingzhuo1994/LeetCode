# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        self.helper(root)
        return root

    def helper(self, node):
        if not node:
            return None
        self.helper(node.right)
        self.total += node.val
        node.val = self.total
        self.helper(node.left)