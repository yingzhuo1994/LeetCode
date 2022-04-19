# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st recursive solution
# O(n) time | O(log(n)) space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        leftTree = self.inorderTraversal(root.left)
        rightTree = self.inorderTraversal(root.right)
        return leftTree + [root.val] + rightTree

# 2nd Iterative solution
# O(n) time | O(n) space
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
