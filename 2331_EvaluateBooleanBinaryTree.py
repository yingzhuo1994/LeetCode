# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if not root.left and not root.right:
            return root.val == 1
        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)


# 2nd solution
# O(n) time | O(h) space
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        match root.val:
            case 0:
                return False
            case 1:
                return True
            case 2:
                return self.evaluateTree(root.left) or self.evaluateTree(root.right)
            case 3:
                return self.evaluateTree(root.left) and self.evaluateTree(root.right)