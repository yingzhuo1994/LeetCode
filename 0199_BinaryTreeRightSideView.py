# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, BFS
# O(n) time | O(n) space
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        ans = []
        while level:
            ans.append(level[-1].val)
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
        return ans

# 2nd solution, DFS
# O(n) time | O(h) space
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.ans = []
        def dfs(node, depth):
            if not node:
                return 
            if depth > len(self.ans):
                self.ans.append(node.val)
            
            if node.right:
                dfs(node.right, depth + 1)
            
            if node.left:
                dfs(node.left, depth + 1)
        
        dfs(root, 1)
        return self.ans