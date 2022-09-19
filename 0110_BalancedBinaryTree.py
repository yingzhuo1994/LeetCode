# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def compareHeight(node):
            if not node:
                return 0, True
            leftHeight, leftIsValid = compareHeight(node.left)
            if not leftIsValid:
                return -1, False
            rightHeight, rightIsValid = compareHeight(node.right)
            if not rightIsValid:
                return -1, False
            
            if abs(leftHeight - rightHeight) <= 1:
                height = max(leftHeight, rightHeight)
                return height + 1, True
            return -1, False
        height, isValid = compareHeight(root)
        return isValid

