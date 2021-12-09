# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftTreeSum = self.treeSum(root.left)
        rightTreeSum = self.treeSum(root.right)
        result = abs(leftTreeSum - rightTreeSum)
        return result + self.findTilt(root.left) + self.findTilt(root.right)

    def treeSum(self, root):
        if not root:
            return 0
        return root.val + self.treeSum(root.left) + self.treeSum(root.right)

# 2nd solution
# O(n) time | O(h) space
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        nodeSum, nodeTiltSum = self.sumAndTiltSum(root)
        return nodeTiltSum

    def sumAndTiltSum(self, root):
        if not root:
            return 0, 0
        leftSum, leftTilt = self.sumAndTiltSum(root.left)
        rightSum, rightTilt = self.sumAndTiltSum(root.right)
        nodeSum = root.val + leftSum + rightSum
        nodeTiltSum = abs(leftSum - rightSum) + leftTilt + rightTilt
        return nodeSum, nodeTiltSum