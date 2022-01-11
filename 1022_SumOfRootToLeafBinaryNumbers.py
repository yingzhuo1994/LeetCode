# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, cur):
        if not node:
            return
         
        cur = (cur << 1) | node.val
        if not node.left and not node.right:
            self.ans += cur
            return 
        
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)