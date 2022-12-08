# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(log(n)) space
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1, []) == self.getLeaves(root2, [])

    def getLeaves(self, node, leaves):
        if not node:
            return leaves
        if node.left:
            self.getLeaves(node.left, leaves)
        if node.right:
            self.getLeaves(node.right, leaves)
        if not node.left and not node.right:
            leaves.append(node.val)
        return leaves