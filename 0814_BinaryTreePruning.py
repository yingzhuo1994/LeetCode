# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, dfs
# O(n) time | O(h) space
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfsPruen(node):
            if not node:
                return False
            
            left = dfsPruen(node.left)
            right = dfsPruen(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
            
            return left or right or node.val == 1
        
        if dfsPruen(root):
            return root
        else:
            return None