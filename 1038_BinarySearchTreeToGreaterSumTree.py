# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        def dfs(node):
            if not node:
                return 0
            if node.right:
                dfs(node.right)

            self.total += node.val
            node.val = self.total
            dfs(node.left)

        
        dfs(root)
        return root