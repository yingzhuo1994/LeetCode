# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node, parent):
            if not node:
                return None
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)
            if not node.left and not node.right:
                if node.val == target:
                    if parent:
                        if parent.left == node:
                            parent.left = None
                        else:
                            parent.right = None
        dfs(root, None)
        if not root.left and not root.right:
            if root.val == target:
                return None
        return root

            
# 2nd solution
# O(n) time | O(h) space
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            root.left = self.removeLeafNodes(root.left, target)
        if root.right:
            root.right = self.removeLeafNodes(root.right, target)
        return None if root.left == root.right and root.val == target else root