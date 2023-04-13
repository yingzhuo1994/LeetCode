# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getTreeStr(node):
            if not node:
                return "None"
            left = getTreeStr(node.left)
            right = getTreeStr(node.right)
            nodeStr = str(node.val) + "#" + left + "#" + right
            if nodeStr == self.ref:
                self.ans = True
            return nodeStr
        self.ref = "Null"
        self.ans = False
        subRootStr = getTreeStr(subRoot)
        self.ref = subRootStr
        rootStr = getTreeStr(root)
        return self.ans