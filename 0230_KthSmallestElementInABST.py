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

        # 2nd solution
        # O(h + k) time | O(h) space
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        treeInfo = TreeInfo(0, -1)
        self.inOrderTraverse(root, treeInfo, k)
        return treeInfo.value
    
    def inOrderTraverse(self, node, treeInfo, k):
        if not node or treeInfo.numOfVisitedNode >= k:
            return
        self.inOrderTraverse(node.left, treeInfo, k)
        if treeInfo.numOfVisitedNode < k:
            treeInfo.numOfVisitedNode += 1
            treeInfo.value = node.val
            self.inOrderTraverse(node.right, treeInfo, k)

class TreeInfo:
    def __init__(self, numOfVisitedNode, value):
        self.numOfVisitedNode = numOfVisitedNode
        self.value = value


