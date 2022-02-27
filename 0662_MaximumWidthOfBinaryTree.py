# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 1
        level = [(root, 0)]
        while level:
            newLevel = []
            if len(level) > 1:
                curWidth = level[-1][1] - level[0][1] + 1
                width = max(width, curWidth)
            for node, num in level:
                if node.left:
                    newLevel.append((node.left, num << 1))
                if node.right:
                    newLevel.append((node.right, num << 1 | 1))
            level = newLevel
        return width