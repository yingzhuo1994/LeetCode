# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1st solution
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

    # 2nd solution
    # O(n^2) time | O(n^2) space
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        self.dfs(root, targetSum, result)
        return result
    
    def dfs(self, node, target, result, path = []):
        if not node:
            return
        value = node.val
        if target == value and not node.left and not node.right:
            path.append(value)
            result.append(path)
            return 
        self.dfs(node.left, target - node.val, result, path + [value])
        self.dfs(node.right, target - node.val, result, path + [value])