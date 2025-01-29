# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        depthDic = {}
        parents = {}
        def dfs(node, depth, parent=None):
            if parent is not None:
                parents[node] = parent
            depthDic[node] = depth
            if node.left:
                dfs(node.left, depth + 1, node)
            if node.right:
                dfs(node.right, depth + 1, node)
        dfs(root, 0)
        deepest = max(depthDic.values())
        level = [node for node in depthDic if depthDic[node] == deepest]
        while len(level) > 1:
            newLevel = set()
            for node in level:
                newLevel.add(parents[node])
            level = newLevel
        ans = level.pop()
        return ans
        
