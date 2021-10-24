# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
    # O(n) time | O(n) space
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        stack = [root]
        while stack:
            count = 0
            newStack = []
            for node in stack:
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
                count += 1
            level += 1
            stack = newStack
        return 2**(level - 1) - 1 + count