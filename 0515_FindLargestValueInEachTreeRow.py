# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(h) space
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, depth=0):
            if not node:
                return
            if len(ans) <= depth:
                ans.append(node.val)
            else:
                ans[depth] = max(ans[depth], node.val)
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
        dfs(root)
        return ans
