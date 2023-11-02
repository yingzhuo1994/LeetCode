# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return [0, 0]
            leftTotal, leftNum = dfs(node.left)
            rightTotal, rightNum = dfs(node.right)
            total = leftTotal + rightTotal + node.val
            num = leftNum + rightNum + 1
            avg = total // num
            if avg == node.val:
                self.ans += 1
            return [total, num]
        
        dfs(root)
        return self.ans