# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
    # O(n) time | O(log(n)) space
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.result = 0
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node, path):
        if not node:
            return
        if not node.left and not node.right:
            self.result += path * 10 + node.val
            return
        self.dfs(node.left, path * 10 + node.val)
        self.dfs(node.right, path * 10 + node.val)
