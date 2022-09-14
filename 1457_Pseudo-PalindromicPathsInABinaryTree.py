# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, bitCount):
            if not node:
                return

            k = node.val - 1
            newCount = bitCount ^ (1 << k)

            if not node.left and not node.right:
                if isPseudoPalindrom(newCount):
                    self.ans += 1
                return
            
            dfs(node.left, newCount)
            dfs(node.right, newCount)
        
        def isPseudoPalindrom(bitCount):
            oddCount = 0
            for i in range(9):
                if bitCount & (1 << i):
                    oddCount += 1

            return oddCount <= 1
        
        dfs(root, 0)
        return self.ans