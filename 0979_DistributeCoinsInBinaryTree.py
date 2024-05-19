# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            self.ans += abs(left) + abs(right)
            node.val += left + right

            if node.val <= 0:
                return 1 - node.val
            elif node.val > 1:
                return -(node.val - 1)
            else:
                return 0
                            
        self.ans = 0
        dfs(root)
        return self.ans


        
        

        