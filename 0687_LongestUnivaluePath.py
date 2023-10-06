# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0

            leftWithRoot = dfs(node.left)
            rightWithRoot  = dfs(node.right)
            
            left = 0
            right = 0

            if node.left and node.left.val == node.val:
                left = leftWithRoot + 1
            if node.right and node.right.val == node.val:
                right = rightWithRoot + 1
            
            self.ans = max(self.ans, left + right)
 
            return max(left, right)

        self.ans = 0
        dfs(root)

        return self.ans