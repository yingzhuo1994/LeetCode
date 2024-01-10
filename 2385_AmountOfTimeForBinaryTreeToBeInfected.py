# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution
# O(n) time | O(n) space
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parents = {}
        def dfs(node, parent):
            if not node:
                return
            parents[node.val] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        startNodeParent = parents[start]
        if startNodeParent is None:
            startNode = root
        else:
            if startNodeParent.left and startNodeParent.left.val == start:
                startNode = startNodeParent.left
            else:
                startNode = startNodeParent.right
        self.ans = 0
        def getMinite(node, prevNode, t):
            if not node:
                return
            self.ans = max(self.ans, t)
            for nextNode in [node.left, node.right, parents[node.val]]:
                if nextNode != prevNode:
                    getMinite(nextNode, node, t + 1)
        getMinite(startNode, None, 0)
        return self.ans