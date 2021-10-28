# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(node, target):
            if not node:
                return []
            if node.val == target and not node.left and not node.right:
                return [[node.val]]
            left = helper(node.left, target - node.val)
            right = helper(node.right, target - node.val)
            return [lst + [node.val] for lst in left + right]
        result = helper(root, targetSum)
        return [lst[::-1] for lst in result]