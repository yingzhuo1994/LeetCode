# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(log(n)) space
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node, num):
        if not node:
            return
        num = num * 10 + node.val
        if not node.left and not node.right:
            self.result += num
            return
        self.dfs(node.left, num)
        self.dfs(node.right, num)
