# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution, recursion
    # O(n) time | O(log(n)) space
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        newTree = TreeNode()
        newTree.val = root1.val + root2.val
        newTree.left = self.mergeTrees(root1.left, root2.left)
        newTree.right = self.mergeTrees(root1.right, root2.right)
        return newTree

    # 2nd solution, iteration
    # O(n) time | O(n) space
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2
        stack = []
        stack.append((root1, root2))
        while stack:
            t = stack.pop();
            if not t[0] or not t[1]:
                continue
            t[0].val += t[1].val
        
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return root1