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
    def preorder(self, root: 'Node') -> List[int]:
        lst = []
        def dfs(node, lst):
            if not node:
                return
            lst.append(node.val)
            for child in node.children:
                dfs(child, lst)
        
        dfs(root, lst)
        return lst
