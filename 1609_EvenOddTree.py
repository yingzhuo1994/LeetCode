# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = [root]
        depth = 0
        while level:
            newLevel = []
            if depth & 1:
                for i in range(len(level) - 1):
                    if level[i].val <= level[i+1].val:
                        return False
                for node in level:
                    if node.val & 1:
                        return False
                    if node.left:
                        newLevel.append(node.left)
                    if node.right:
                        newLevel.append(node.right)
            else:
                for i in range(len(level) - 1):
                    if level[i].val >= level[i+1].val:
                        return False
                for node in level:
                    if not (node.val & 1):
                        return False
                    if node.left:
                        newLevel.append(node.left)
                    if node.right:
                        newLevel.append(node.right)
            level = newLevel
            depth += 1
        return True
