# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            leftSubtreeInfo = helper(node.left, lower, node.val)
            rightSubtreeInfo = helper(node.right, node.val, upper)
            if lower < node.val < upper and leftSubtreeInfo and rightSubtreeInfo:
                return True
            else:
                return False

        return helper(root)

