# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(log(n)) space
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    result += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result


# 2nd solution
# O(n) time | O(log(n)) space
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node, side):
        if not node:
            return 
        if not node.left and not node.right and side == -1:
            self.result += node.val
        
        self.dfs(node.left, -1)
        self.dfs(node.right, 1)
        