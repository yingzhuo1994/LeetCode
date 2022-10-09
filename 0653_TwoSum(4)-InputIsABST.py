# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.memo = set()
        def dfs(node):
            if not node:
                return False
            self.memo.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        def dfs_check(node, target):
            if not node:
                return False
            val = node.val
            curTarget = target - val
            if curTarget in self.memo and curTarget != val:
                return True
            return dfs_check(node.left, target) or dfs_check(node.right, target)
        dfs(root)
        return dfs_check(root, k)
        
        
        