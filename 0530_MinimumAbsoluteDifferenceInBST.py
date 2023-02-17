# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
# where n is number of nodes and h is the height of the tree
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        self.lastVal = float("-inf")

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            diff = node.val - self.lastVal
            self.ans = min(self.ans, diff)
            self.lastVal = node.val
            dfs(node.right)

        dfs(root)
        return self.ans