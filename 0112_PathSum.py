# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, DFS
# O(n) time | O(h) space
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum)
    
    def dfs(self, node, target, curSum=0):
        if not node:
            return False
        value = node.val
        curSum += value
        if not node.left and not node.right:
            if curSum == target:
                return True
        return self.dfs(node.left, target, curSum) or self.dfs(node.right, target, curSum)