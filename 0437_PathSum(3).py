# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        stack = [root]
        count = 0
        while stack:
            curNode = stack.pop()
            if curNode:
                count += self.pathSumHelper(curNode, targetSum)
                stack.append(curNode.left)
                stack.append(curNode.right)
        return count

    def pathSumHelper(self, node, targetSum):
        if not node:
            return 0
        count = 0
        if node.val == targetSum:
            count += 1
        count += self.pathSumHelper(node.left, targetSum - node.val)
        count += self.pathSumHelper(node.right, targetSum - node.val)
        return count