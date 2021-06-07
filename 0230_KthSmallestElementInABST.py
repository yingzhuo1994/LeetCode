# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 1st solution
        # O(nlogn) time | O(n) space 
        lst = []
        level = [root]
        while level:
            curLevel = []
            for node in level:
                lst.append(node.val)
                if node.left:
                    curLevel.append(node.left)
                if node.right:
                    curLevel.append(node.right)
            level = curLevel
        lst.sort()
        return lst[k - 1]

class treeInfo:
    def __init__(self, numOfVisitedNode):
        self.numOfVisistedNode = numOfVisitedNode


