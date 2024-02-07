# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sumDic = {}
        def dfs(node, depth):
            if not node:
                return
            sumDic[depth] = sumDic.get(depth, 0) + node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        def dfs_replace(node, depth):
            if not node:
                return
            value = 0
            if node.left:
                value += node.left.val
            if node.right:
                value += node.right.val
            
            newValue = sumDic.get(depth + 1, 0) - value
            if node.left:
                node.left.val = newValue
            if node.right:
                node.right.val = newValue
            
            dfs_replace(node.left, depth + 1)
            dfs_replace(node.right, depth + 1)
        
        dfs(root, 0)
        dfs_replace(root, 0)
        root.val = 0
        return root