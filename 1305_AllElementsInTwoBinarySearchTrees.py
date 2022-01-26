# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arrayOne = self.getElements(root1)
        arrayTwo = self.getElements(root2)
        res = []
        i, j = 0, 0
        while i < len(arrayOne) and j < len(arrayTwo):
            if arrayOne[i] < arrayTwo[j]:
                res.append(arrayOne[i])
                i += 1
            else:
                res.append(arrayTwo[j])
                j += 1
        res.extend(arrayOne[i:] or arrayTwo[j:])
        return res
  
    def getElements(self, root):
        if not root:
            return []
        return self.getElements(root.left) + [root.val] + self.getElements(root.right)