# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
    # O(n) time | O(log(n)) space
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        newTree = TreeNode()
        newTree.val = root1.val + root2.val
        newTree.left = self.mergeTrees(root1.left, root2.left)
        newTree.right = self.mergeTrees(root1.right, root2.right)
        return newTree