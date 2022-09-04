# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n^2 * log(n)) time | O(n) space
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnDict = defaultdict()
        leftMost = rightMost = 0
        stack = [[root, 0, 0]]
        while stack:
            node, row, col = stack.pop()
            leftMost = min(leftMost, col)
            rightMost = max(rightMost, col)

            if col not in columnDict:
                columnDict[col] = {}
            if row not in columnDict[col]:
                columnDict[col][row] = []
            columnDict[col][row].append(node.val)

            if node.right:
                stack.append([node.right, row + 1, col + 1])
            if node.left:
                stack.append([node.left, row + 1, col - 1])
        
        ans = []
        for col in range(leftMost, rightMost + 1):
            rowDict = columnDict[col]
            rows = sorted(rowDict.keys())
            lst = []
            for row in rows:
                lst.extend(sorted(rowDict[row]))
            ans.append(lst)
        
        return ans
        
