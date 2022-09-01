# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, DFS
# O(n) time | O(h) space
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, float("-inf"))
        return self.count
    
    def dfs(self, node, maxValue):
        if not node:
            return
        if node.val >= maxValue:
            self.count += 1
        maxValue = max(node.val, maxValue)
        self.dfs(node.left, maxValue)
        self.dfs(node.right, maxValue)
