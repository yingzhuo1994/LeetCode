# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        withRoot, _ = self.maxSum(root)
        return withRoot
    
    def maxSum(self, node):
        if not node:
            return 0, 0

        leftWithNode, leftWithoutNode = self.maxSum(node.left)
        rightWithNode, rightWithoutNode = self.maxSum(node.right)

        withRoot = node.val + leftWithoutNode + rightWithoutNode
        withoutRoot = leftWithNode + rightWithNode
        return  max(withRoot, withoutRoot), withoutRoot