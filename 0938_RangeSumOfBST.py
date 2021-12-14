# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(h) space
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.dfs(root, low, high)
        return self.ans
    
    def dfs(self, node, low, high):
        if not node:
            return 
        if low <= node.val <= high:
            self.ans += node.val
        
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)