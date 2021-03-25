# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)

    def helper(self, L, R):
        if L is not None and R is not None:
            if L.val != R.val:
                return False
            else:
                return self.helper(L.left, R.right) and self.helper(L.right, R.left)
        elif (L and not R) or (not L and R):
            return False
        else:
            return True
