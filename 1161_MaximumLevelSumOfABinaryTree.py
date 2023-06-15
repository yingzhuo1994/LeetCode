# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1st solution, bfs
# O(n) time | O(n) space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 0
        value = float("-inf")

        stack = [root]
        depth = 1
        while stack:
            newStack = []
            curSum = 0
            for node in stack:
                curSum += node.val
                if node.left:
                    newStack.append(node.left)
                if node.right:
                    newStack.append(node.right)
            if curSum > value:
                value = curSum
                level = depth
            depth += 1
            stack = newStack
        return level

# 2nd solution, dfs
# O(n) time | O(n) space
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dic = {}

        def dfs(node, depth):
            if not node:
                return
            dic[depth] = dic.get(depth, 0) + node.val
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        depth = 1
        level = 0
        value = float("-inf")
        while depth in dic:
            if dic[depth] > value:
                value = dic[depth]
                level = depth
            depth += 1
        return level