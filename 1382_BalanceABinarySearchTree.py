# 1st solution
# O(n) time | O(n) space

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.vals.append(node.val)
            dfs(node.right)
        
        def buildTree(start, end):
            if start > end:
                return None
            idx = start + (end - start) // 2
            node = TreeNode(self.vals[idx])
            node.left = buildTree(start, idx - 1)
            node.right = buildTree(idx + 1, end)
            return node
        
        self.vals = []
        dfs(root)
        
        return buildTree(0, len(self.vals) - 1)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right