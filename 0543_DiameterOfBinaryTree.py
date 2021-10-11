# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, longest = self.diameter(root)
        return longest - 1
    
    def diameter(self, node):
        if not node:
            return 0, 0
        
        maxLeftLengthChildren, maxLeftLength = self.diameter(node.left)
        maxRightLengthChildren, maxRightLength = self.diameter(node.right)
        maxLengthChildren = max(maxLeftLengthChildren, maxRightLengthChildren)

        maxRootLengthChildren = maxLengthChildren + 1
        maxRootLength = max(maxLeftLengthChildren + 1 + maxRightLengthChildren, maxRootLengthChildren)
        maxLength = max(maxLeftLength, maxRightLength, maxRootLength)
        return maxRootLengthChildren, maxLength