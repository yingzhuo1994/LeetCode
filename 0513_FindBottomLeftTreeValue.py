# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st soluton, BFS
# O(n) time | O(n) space
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        while stack:
            newStack = []
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if not newStack:
                return stack[0].val
            stack = newStack
        return None