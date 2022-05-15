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
            ans = 0
            newLevel = []
            for node in level:
                ans += node.val
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            if len(newLevel) == 0:
                return ans
            level = newLevel