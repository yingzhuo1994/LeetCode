# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return -1, -1
            leftLeft, leftRight = dfs(node.left)
            rightLeft, rightRight = dfs(node.right)
            left = leftRight + 1
            right = rightLeft + 1
            self.ans = max(self.ans, left, right, leftLeft, rightRight)
            return left, right
        dfs(root)
        return self.ans

# 2nd solution
# O(n) time | O(h) space
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return -1, -1, 0
            leftLeft, leftRight, leftMax = dfs(node.left)
            rightLeft, rightRight, rightMax = dfs(node.right)
            left = leftRight + 1
            right = rightLeft + 1
            ans = max(left, right, leftMax, rightMax)
            return left, right, ans
        return dfs(root)[-1]