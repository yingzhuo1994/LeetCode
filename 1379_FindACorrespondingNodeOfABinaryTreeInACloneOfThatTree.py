# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1st solution
# O(n) time | O(h) space
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.clonedTargetNode = None
        def dfs(tree1, tree2, target):
            if not tree1:
                return 
            if tree1 == target:
                self.clonedTargetNode = tree2
                return
            if self.clonedTargetNode is not None:
                return
            dfs(tree1.left, tree2.left, target)
            dfs(tree1.right, tree2.right, target)
        
        dfs(original, cloned, target)
        return self.clonedTargetNode