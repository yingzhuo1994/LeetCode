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

# 2nd soluton, DFS
# O(n) time | O(h) space
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.maxDepth = 0
        self.getValue = False
        self.ans = None
        def dfs(node, depth=0):
            if not node:
                return
            self.maxDepth = max(self.maxDepth, depth)
            if node.left:
                dfs(node.left, depth + 1)
            
            if node.right:
                dfs(node.right, depth + 1)
            
            if self.getValue and self.maxDepth == depth:
                self.ans = node.val
                self.getValue = False
        dfs(root)
        self.getValue = True
        dfs(root)
        return self.ans