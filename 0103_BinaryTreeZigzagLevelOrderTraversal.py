# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        level = [root] if root else []
        lst = []
        seqMark = 1
        while level:
            curLst = []
            curLevel = []

            for node in level:
                curLst.append(node.val)
                if node.left:
                    curLevel.append(node.left)
                if node.right:
                    curLevel.append(node.right)
            if seqMark > 0:
                lst.append(curLst)
            else:
                lst.append(curLst[::-1])
            level = curLevel
            seqMark *= -1
        return lst
