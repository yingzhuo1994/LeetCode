# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st recursive solution
# O(n) time | O(h) space
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

# 2nd iterative solution
# O(n) time | O(h) space
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val: 
                return False
            pre = root
            root = root.right
        return True
