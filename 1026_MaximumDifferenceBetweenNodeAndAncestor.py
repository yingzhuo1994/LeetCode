# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.searchWithMaxMin(root, root.val, root.val)
        return self.ans
    
    def searchWithMaxMin(self, node, greatest, smallest):
        if not node:
            diff = greatest - smallest
            self.ans = max(self.ans, diff)
            return 

        greatest = max(greatest, node.val)
        smallest = min(smallest, node.val)
        self.searchWithMaxMin(node.left, greatest, smallest)
        self.searchWithMaxMin(node.right, greatest, smallest)
