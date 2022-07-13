# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, BFS
# O(n) time | O(n) space
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        level = [root] if root else []
        lst = []
        while level:
            curLst = []
            curLevel = []
            for node in level:
                curLst.append(node.val)
                if node.left:
                    curLevel.append(node.left)
                if node.right:
                    curLevel.append(node.right)
            lst.append(curLst)
            level = curLevel
        return lst