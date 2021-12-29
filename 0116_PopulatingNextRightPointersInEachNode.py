"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 1st stack solution
# O(n) time | O(n) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = [root] if root else []
        while level:
            curLevel = []
            for i in range(len(level)):
                if i < len(level) - 1:
                    level[i].next = level[i + 1]
                if level[i].left:
                    curLevel.append(level[i].left)
                if level[i].right:
                    curLevel.append(level[i].right)
            level = curLevel
        return root

# 2nd solution
# O(n) time | O(1) space
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head = root
        while root and root.left:
            nextLevelNode = root.left 
            while root:
                root.left.next = root.right 
                # root.right.next = root.next and root.next.left
                if root.next:
                    root.right.next = root.next.left 
                root = root.next
            root = nextLevelNode
        return head