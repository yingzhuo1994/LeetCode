# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, s):
            if not node:
                return

            ch = chr(node.val + ord("a")) 
            s = ch + s

            if not node.left and not node.right:
                if self.ans is None:
                    self.ans = s
                elif s < self.ans:
                    self.ans = s
                return 
            
            if node.left:
                dfs(node.left, s)
            if node.right:
                dfs(node.right, s)

        self.ans = None
        dfs(root, "")

        return self.ans