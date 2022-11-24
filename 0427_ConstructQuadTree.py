"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

# 1st solution
# O(n^2) time | O(n^2) space
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(row1, row2, col1, col2):
            k = row2 - row1
            count = dp[row1][col1] - dp[row1][col2] - dp[row2][col1] + dp[row2][col2]
            root = Node(0, False, None, None, None, None)
            root.val = count == k * k

            if count == 0 or count == k * k:
                root.isLeaf = True
            else:
                midRow = row1 + (row2 - row1) // 2
                midCol = col1 + (col2 - col1) // 2
                root.topLeft = helper(row1, midRow, col1, midCol)
                root.topRight = helper(row1, midRow, midCol, col2)
                root.bottomLeft = helper(midRow, row2, col1, midCol)
                root.bottomRight = helper(midRow, row2, midCol, col2)
            return root
        
        n = len(grid)
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1] + grid[i][j]
        
        return helper(0, n, 0, n)