# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node):
            if not node:
                return None
                        
            left = node.left
            right = node.right
            node.left = None
            if left:
                tail = helper(left)
                node.right = left
                node = tail
            if not right:
                return node
            node.right = right
            return helper(node.right)
        helper(root)

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                runner = curr.left
                while runner.right: runner = runner.right
                runner.right, curr.right, curr.left = curr.right, curr.left, None
            curr = curr.right

# 3rd solution, Morris Traversal
# O(n) time | O(1) space
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curNode = root
        while curNode:
            if curNode.left:
                node = curNode.left
                while node.right and node.right != curNode:
                    node = node.right
                if not node.right:
                    node.right = curNode
                    # print(curNode.val)
                    nextNode = curNode.left
                else:
                    node.right = curNode.right
                    nextNode = curNode.right
                    curNode.right = curNode.left
                    curNode.left = None
            else:
                # print(curNode.val)
                nextNode = curNode.right
            curNode = nextNode