# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            return self.helper(root.left, root.right)

    # 1st recursive solution
    # O(n) time | O(h) time (worst O(n) time)
    def helper(self, L, R):
        if L is not None and R is not None:
            if L.val != R.val:
                return False
            else:
                return self.helper(L.left, R.right) and self.helper(L.right, R.left)
        elif (L and not R) or (not L and R):
            return False
        else:
            return True

    # 2nd iterative solution
    # O(n) time | O(n) time
    def helper(self, L, R):
        stack = [L, R]
        while len(stack) > 0:
            curStack = []
            for i in range(len(stack) // 2):
                left = stack[2 * i]
                right = stack[2 * i + 1]
                if left is None and right is None:
                    continue
                elif left is None or right is None or left.val != right.val:
                    return False
                elif left.val == right.val:
                    temp = [left.left, right.right, left.right, right.left]
                    curStack.extend(temp)
            stack = curStack
        return True
