# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
    # O(n) time | O(log(n)) space
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, maxNodeNumber = self.getNodeNumber(root)
        return maxNodeNumber - 1
    
    def getNodeNumber(self, node):
        if not node:
            return 0, 0
        
        maxLeftLengthChildren, maxLeftLength = self.getNodeNumber(node.left)
        maxRightLengthChildren, maxRightLength = self.getNodeNumber(node.right)
        maxLengthChildren = max(maxLeftLengthChildren, maxRightLengthChildren)

        maxRootLengthChildren = maxLengthChildren + 1
        maxRootLength = maxLeftLengthChildren + 1 + maxRightLengthChildren
        maxLength = max(maxLeftLength, maxRightLength, maxRootLength)
        return maxRootLengthChildren, maxLength