"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 1st solution, recursive
# O(n) time | O(n) space
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))
        ans.append(root.val)
        return ans


# 2nd solution, iterative
# O(n) time | O(n) space
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        level = [root]
        ans = []
        while level:
            node = level.pop()
            if not node:
                continue
            ans.append(node.val)
            level.extend(node.children)
        return ans[::-1]