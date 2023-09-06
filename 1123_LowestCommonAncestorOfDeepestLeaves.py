# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parents = {root: None}
        level = [root]
        while level:
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                    parents[node.left] = node
                if node.right:
                    newLevel.append(node.right)
                    parents[node.right] = node
            if not newLevel:
                break

            level = newLevel
        
        ans = set(level)
        while len(ans) > 1:
            new = set()
            for node in ans:
                p = parents[node]
                new.add(p)
            ans = new
        
        return list(ans)[0]
