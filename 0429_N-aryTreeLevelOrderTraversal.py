"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 1st solution, dfs
# O(n) time | O(n) space 
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [[root, 0]]
        while stack:
            node, depth = stack.pop()
            if depth == len(ans):
                ans.append([])
            ans[depth].append(node.val)

            for child in reversed(node.children):
                stack.append([child, depth + 1])
        return ans
