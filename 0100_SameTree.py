# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, recursion
# O(n) time | O(h) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p:
            return False
        if not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

# 2nd solution, iteration
# O(n) time | O(n) space
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = [p]
        qStack = [q]
        while pStack and qStack:
            pNode = pStack.pop()
            qNode = qStack.pop()
            if not pNode and not qNode:
                continue
            if not pNode:
                return False
            if not qNode:
                return False
            if pNode.val != qNode.val:
                return False
            pStack.append(pNode.right)
            pStack.append(pNode.left)
            qStack.append(qNode.right)
            qStack.append(qNode.left)
        return len(pStack) == len(qStack)