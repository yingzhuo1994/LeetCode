# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def getDepth(node):
            if not node:
                return 0
            leftHeight = getDepth(node.left)
            rightHeight = getDepth(node.right)
            height = max(leftHeight, rightHeight) + 1

            return height
        
        m = getDepth(root)
        n = pow(2, m) - 1
        matrix = [["" for _ in range(n)] for _ in range(m)]

        def dfs(node, row, start, end):
            if not node:
                return
            mid = start + (end - start) // 2
            matrix[row][mid] = str(node.val)
            dfs(node.left, row + 1, start, mid - 1)
            dfs(node.right, row + 1, mid + 1, end)
        
        dfs(root, 0, 0, n - 1)

        return matrix

