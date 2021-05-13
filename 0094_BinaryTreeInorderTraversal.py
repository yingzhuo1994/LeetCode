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
        p = root
        if not p:
            return []
        elif not p.left and not p.right:
            return [p.val]
        leftTree = self.inorderTraversal(p.left)
        rightTree = self.inorderTraversal(p.right)
        return leftTree + [p.val] + rightTree
