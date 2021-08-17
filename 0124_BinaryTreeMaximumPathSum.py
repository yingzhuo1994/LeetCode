# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time | O(log(n)) space
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        _, maxSum = self.getMaxPathSum(root)
        return maxSum
    
    def getMaxPathSum(self, node):
        if not node:
            return float('-inf'), float('-inf')
        
        leftMaxSumAsBranch, leftMaxPathSum = self.getMaxPathSum(node.left)
        rightMaxSumAsBranch, rightMaxPathSum = self.getMaxPathSum(node.right)
        maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

        value = node.val
        maxSumAsBranch = max(maxChildSumAsBranch + value, value)
        maxSumAsRootNode = max(leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch)
        maxPathSum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

        return (maxSumAsBranch, maxPathSum)
