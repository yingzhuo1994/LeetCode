# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.ans = []
        def dfs(node):
            if not node:
                return
            self.ans.append(str(node.val))
            if node.left:
                self.ans.append("(")
                dfs(node.left)
                self.ans.append(")")
            
            if not node.left and node.right:
                self.ans.append("()")
            if node.right:
                self.ans.append("(")
                dfs(node.right)
                self.ans.append(")")
    
        dfs(root)
        return "".join(self.ans)