# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 1st recursive solution
        # O(n) time | O(logn) space
        if not root:
            return []
        leftTree = self.inorderTraversal(root.left)
        rightTree = self.inorderTraversal(root.right)
        return leftTree + [root.val] + rightTree
