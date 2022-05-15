# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, BFS
# O(n) time | O(n) space
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while True:
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            if len(newLevel) == 0:
                break
            level = newLevel
        return sum([node.val for node in level])