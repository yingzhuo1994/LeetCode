# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
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


# 2nd solution
# O(log(n) * log(n)) time | O(log(n)) space
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)

# 3rd solution, iteration
# O(log(n) * log(n)) time | O(1) space
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        node = root
        count = 0
        while node:
            left = self.getDepth(node.left)
            right = self.getDepth(node.right)
            if left == right:
                count += 2**left
                node = node.right
            else:
                count += 2**right
                node = node.left
        return count

    def getDepth(self, root):
        depth = 0
        while root:
            depth += 1
            root = root.left
        return depth