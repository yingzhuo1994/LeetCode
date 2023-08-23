# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        minVal = root.val
        def dfs(node):
            if not node:
                return
            if node.val != minVal:
                self.ans = min(self.ans, node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if self.ans == float("inf"):
            return -1
        return self.ans

# 2nd solution
# O(n) time | O(h) space
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.ans = float("inf")
        minVal = root.val
        def dfs(node):
            if not node:
                return
            if node.val > self.ans:
                return
            if node.val != minVal:
                self.ans = min(self.ans, node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        if self.ans == float("inf"):
            return -1
        return self.ans